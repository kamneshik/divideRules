from loguru import logger

start_log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

log_format_info = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level> | "
    "path: <cyan>{extra[path]}</cyan> | "
    "Time Elapsed: <cyan>{extra[time_elapsed]}</cyan> | "
    "Time: <cyan>{time}</cyan> | "
)

log_format_error = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "Error: {message}"
    "End Time: <cyan>{extra[end_time]}</cyan> | "
)

logger.configure(
    handlers=[
        {
            "sink": "logs/app.log",
            "rotation": "1 week",
            "format": start_log_format,
            "level": "STARTAPP",
        },
        {
            "sink": "logs/app.log",
            "rotation": "1 week",
            "format": log_format_info,
            "level": "INFO",
        },
{
            "sink": "logs/app.log",
            "rotation": "1 week",
            "format": log_format_info,
            "level": "SUCCESS",
        },
        {
            "sink": "logs/errors.log",
            "level": "ERROR",
            "format": log_format_error,
            "rotation": "1 week",
        },
    ],
    levels=[dict(name="STARTAPP", no=13, icon="¤", color="")]

)
