import os
from typing import List


class CommonConfig:
    ENVIRONMENT:str = os.environ['ENVIRONMENT']
    LOG_LEVEL:str= os.environ['LOG_LEVEL'].upper()
    ALLOWED_ORIGINS:List[str] = os.getenv("ALLOWED_ORIGINS", "").split(",")
