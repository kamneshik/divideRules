from aiohttp import web
import time
from log_config import logger
from middleware.request_logger_middleware import request_logger_middleware
from routes import setup_routes

if __name__ == "__main__":
    app = web.Application()
    app.middlewares.append(request_logger_middleware)
    setup_routes(app)
    #logger.log("STARTAPP", "Starting app ...")
    web.run_app(app)
