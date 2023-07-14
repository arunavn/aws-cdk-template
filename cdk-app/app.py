#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_app.cdk_app_stack import CdkAppStack
from config import app_config


app = cdk.App()
app_config_obj = app_config.Config()
CdkAppStack(app, app_config_obj.stack_name(),
    env=cdk.Environment(account='700433791282', region='us-east-1'),
    )

app.synth()
