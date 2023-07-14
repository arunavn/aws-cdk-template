from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct
from config import app_config
class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        app_config_obj = app_config.Config()
        # example resource
        queue = sqs.Queue(
            self, "CdkAppQueue",
            visibility_timeout=Duration.seconds(300),
        )
