import os
from typing import List, Literal


class CommonConfig:
    ENVIRONMENT:str = os.environ['ENVIRONMENT']
    LOG_LEVEL:str= os.environ['LOG_LEVEL'].upper()
    ALLOWED_ORIGINS:List[str] = os.getenv("ALLOWED_ORIGINS", "").split(",")
    COOKIE_HTTP_ONLY: bool = os.environ['COOKIE_HTTP_ONLY']
    COOKIE_SAMESITE:Literal['Strict','Lax','None']  = os.environ['COOKIE_SAMESITE']
    COOKIE_SECURE:bool = os.environ['COOKIE_SECURE']
