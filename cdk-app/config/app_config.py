import os
import json


class Config:
    def __init__(self) -> None:
        with open('config/app_config.json', 'r') as f:
            self.config_dict = json.load(f)
        self.deploy_env =  os.environ['DEPLOY_ENV']
        self.env_dict = self.config_dict.get(self.deploy_env, None)
    
    def account_id(self) -> str:
        return self.env_dict.get('accountId', '')