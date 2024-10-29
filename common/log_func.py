import logging
from logging.config import dictConfig
from pathlib import Path
Path("data/logs").mkdir(parents=True, exist_ok=True)
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format':'[%(asctime)s][%(threadName)s:%(thread)d]%(process)s[task_id:%(name)s][%(filename)s:%(lineno)d][%(levelname)s][%(message)s]',
        }
    },
    "handlers": {
        "rotate_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "when": "midnight",
            "formatter": "default",
            "filename": 'data/logs/worm.log'
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default"
        },
    },
    "loggers": {
        "root_loger": {
            "handlers": ["rotate_file", "console"],
            "level": "INFO",
        },
        "example_loger": {
            "handlers": ["rotate_file", "console"],
            "level": "INFO",
            "qualname": "example",
            "propagate": False,
        }
    },
    "disable_existing_loggers": True,
}


class ZeroLog:

    def info(self, aa):
        pass

    def exception(self, bb):
        pass


dictConfig(LOGGING_CONFIG)
LOG = logging.getLogger("example_loger")
LOG.setLevel(logging.INFO)
# LOG = ZeroLog()
logging.getLogger().setLevel(logging.ERROR)
