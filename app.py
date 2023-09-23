from aiohttp import web
import time
from log_config import logger as config_logger
from middleware import request_logger_middleware


if __name__ == "__main__":
    app = web.Application(middleware=[request_logger_middleware])

    config_logger.info("Starting the app ...")
    web.run_app()
