from loguru import logger

log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level> | "
    "Method: <cyan>{extra[method]}</cyan> | "
    "Path: <cyan>{extra[path]}</cyan> | "
    "Status: <cyan>{extra[status]}</cyan> | "
    "Time Elapsed: <cyan>{extra[time_elapsed]}</cyan> | "
    "End Time: <cyan>{extra[end_time]}</cyan> | "
    "Function: <cyan>{extra[function]}</cyan>"
)


logger.configure(
    handlers=[
        {
            "sink": "logs/app.log",
            "format": log_format,
            "rotation": "1 week",
        },
        {
            "sink": "logs/errors.log",
            "level": "ERROR",
            "format": log_format,
            "rotation": "1 week",
        },
    ],
    level="INFO"
)
