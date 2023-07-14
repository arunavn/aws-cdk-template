#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_app.cdk_app_stack import CdkAppStack


app = cdk.App()
CdkAppStack(app, "CdkAppStack",
    env=cdk.Environment(account='700433791282', region='us-east-1'),
    )

app.synth()
