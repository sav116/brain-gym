from pydantic import BaseModel
from environs import Env
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

env = Env()
env.read_env()

config_data = {
    "bot_token": env.str("BOT_TOKEN"),
    "admins": env.list("ADMINS"),
}

class Config(BaseModel):
    bot_token: str
    admins: list
    
config = Config(**config_data)