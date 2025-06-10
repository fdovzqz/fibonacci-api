#!/usr/bin/env python3
import aws_cdk as cdk
from fibonacci_stack import FibonacciStack

app = cdk.App()
FibonacciStack(app, "FibonacciStack")

app.synth()