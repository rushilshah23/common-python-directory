import logging
import sys
from pythonjsonlogger import jsonlogger
from common.configs.env import CommonConfig
from asgi_correlation_id import correlation_id

class CorrelationIdFilter(logging.Filter):
    """Inject correlation_id into every log record."""
    def filter(self, record):
        record.correlation_id = correlation_id.get() or "N/A"
        return True


def get_logger(name: str) -> logging.Logger:
    """
    Universal JSON logger for FastAPI microservices.
    - Same format in DEV & PROD
    - Structured JSON logs (ideal for Fluentd, Loki, ELK, etc.)
    - Configurable log level via CommonConfig.LOG_LEVEL
    """
    log_level = CommonConfig.LOG_LEVEL
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if logger.hasHandlers():
        return logger

    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(CorrelationIdFilter())

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        rename_fields={
            "asctime": "timestamp",
            "levelname": "level",
            "name": "logger",
            "message": "msg"
        },
        json_ensure_ascii=False,
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
