import logging
import logging.config

from gunicorn.glogging import Logger

from .config import config

loglevel = logging.ERROR if config.stage == "prod" else logging.DEBUG

DEFAULT_LOG_FORMAT = "[%(asctime)s.%(msecs)03d] %(levelname)-7s %(name)10s:%(module)s.%(funcName)s:%(lineno)d - %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

log_config = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": DEFAULT_LOG_FORMAT,
            "datefmt": DEFAULT_DATE_FORMAT,
        },
    },
    "handlers": {
        "default": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "formatter": "default",
        },
    },
    "loggers": {
        "app": {
            "level": "INFO",
            "handlers": ["default"],
            "propagate": False,
            "qualname": "app",
        },
        "app.error": {
            "level": "ERROR",
            "handlers": ["error"],
            "propagate": False,
            "qualname": "app.error",
        },
    },
    "root": {"handlers": ["default"], "level": loglevel},
}


def setup_logger():
    logging.config.dictConfig(log_config)


class GunicornLogger(Logger):
    def setup(self, cfg) -> None:
        super().setup(cfg)

        self._set_handler(
            log=self.access_log,
            output=cfg.accesslog,
            fmt=logging.Formatter(fmt=DEFAULT_LOG_FORMAT, datefmt=DEFAULT_DATE_FORMAT),
        )
        self._set_handler(
            log=self.error_log,
            output=cfg.errorlog,
            fmt=logging.Formatter(fmt=DEFAULT_LOG_FORMAT, datefmt=DEFAULT_DATE_FORMAT),
        )
