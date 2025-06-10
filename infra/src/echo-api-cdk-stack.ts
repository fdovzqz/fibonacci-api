import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apprunner from 'aws-cdk-lib/aws-apprunner';
import * as iam from 'aws-cdk-lib/aws-iam';

export class EchoApiCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Crear rol de servicio para App Runner
    const serviceRole = new iam.Role(this, 'AppRunnerServiceRole', {
      assumedBy: new iam.ServicePrincipal('build.apprunner.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSAppRunnerServicePolicyForECRAccess'),
      ],
    });

    // Crear rol de instancia para App Runner
    const instanceRole = new iam.Role(this, 'AppRunnerInstanceRole', {
      assumedBy: new iam.ServicePrincipal('tasks.apprunner.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSAppRunnerServicePolicyForECRAccess'),
      ],
    });

    // Configuración básica de App Runner
    const appRunnerService = new apprunner.CfnService(this, 'EchoApiService', {
      serviceName: 'echo-api-service',
      sourceConfiguration: {
        autoDeploymentsEnabled: true,
        authenticationConfiguration: {
          accessRoleArn: serviceRole.roleArn,
        },
        codeRepository: {
          codeConfiguration: {
            configurationSource: 'REPOSITORY',
          },
          repositoryUrl: 'https://github.com/fdovzqz/echo-docker.git', // Cambiar por tu repositorio
          sourceCodeVersion: {
            type: 'BRANCH',
            value: 'main',
          },
        },
      },
      instanceConfiguration: {
        instanceRoleArn: instanceRole.roleArn,
        cpu: '1 vCPU',
        memory: '2 GB',
      },
    });

    // Output básico
    new cdk.CfnOutput(this, 'AppRunnerServiceUrl', {
      value: appRunnerService.attrServiceUrl,
      description: 'URL del servicio App Runner',
    });
  }
} 