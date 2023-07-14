import os
import json


class Config:
    def __init__(self) -> None:
        with open('config/app_config.json', 'r') as f:
            self.config_dict = json.load(f)
        self.deploy_env =  os.environ['DEPLOY_ENV']
        self.env_dict = self.config_dict.get(self.deploy_env, None)
    
    def stack_name(self) -> str:
        return self.config_dict.get('stackName', '')
    
    def account_id(self) -> str:
        return self.env_dict.get('accountId', '')
    
    def deploy_region(self) -> str:
        return self.env_dict['primaryRegion'] 

    def generate_resource_name(self, resource_name) -> str:
        stack_prefix, region = self.config_dict['stackPrefix'], self.deploy_region()
        return f"{stack_prefix}-{resource_name}-{self.deploy_env}-{region}"
    
    def generate_resource_id(self, resource_id) -> str:
        stack_prefix, region = self.config_dict['stackPrefix'], self.self.deploy_region()
        region = region.replace('-', '')
        return f"{stack_prefix}{resource_id}{self.deploy_env}{region}"