from log_config import logger
import time


async def request_logger_middleware(app, handler):
    async def middleware_handler(request):
        start_time = time.time()
        try:
            responce = await handler(request)
            status = responce.status
        except Exception as e:
            status = 500
            logger.error("Error occured: {}", e)
            raise e
        finally:
            end_time = time.time()
            elapsed_time = end_time - start_time
            log_entry = {
                "path": request.path,
                "status": status,
                "time_elapsed": elapsed_time,
            }
            logger.success(
                "Request processed",
                path=request.path,
                status=str(status),
                time_elapsed=elapsed_time,
                end_time=end_time,
            )
        return responce
    return middleware_handler
