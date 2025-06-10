from aws_cdk import (
    Stack,
    aws_apprunner as apprunner,
    aws_iam as iam,
)
from constructs import Construct

class FibonacciStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM Role para App Runner
        app_runner_role = iam.Role(
            self, "AppRunnerRole",
            assumed_by=iam.ServicePrincipal("build.apprunner.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSAppRunnerServicePolicyForECRAccess"
                )
            ]
        )

        # App Runner Service
        app_runner_service = apprunner.CfnService(
            self, "FibonacciAppRunnerService",
            source_configuration=apprunner.CfnService.SourceConfigurationProperty(
                auto_deployments_enabled=True,
                code_repository=apprunner.CfnService.CodeRepositoryProperty(
                    repository_url="https://github.com/fdovzqz/echo-docker.git",
                    source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                        type="BRANCH",
                        value="main"
                    ),
                    code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                        configuration_source="REPOSITORY",
                        code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                            runtime="PYTHON_3",
                            build_command="pip install -r requirements.txt",
                            start_command="gunicorn --bind 0.0.0.0:8000 app:app",
                            runtime_environment_variables=[
                                apprunner.CfnService.KeyValuePairProperty(
                                    name="PORT",
                                    value="8000"
                                )
                            ]
                        )
                    )
                )
            ),
            service_name="fibonacci-api",
            instance_configuration=apprunner.CfnService.InstanceConfigurationProperty(
                cpu="0.25 vCPU",
                memory="0.5 GB"
            ),
            health_check_configuration=apprunner.CfnService.HealthCheckConfigurationProperty(
                protocol="HTTP",
                path="/health",
                interval=10,
                timeout=5,
                healthy_threshold=1,
                unhealthy_threshold=5
            )
        )