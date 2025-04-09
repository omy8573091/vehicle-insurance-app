import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging():
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Main logger configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(
                "logs/app.log", maxBytes=1024 * 1024 * 5, backupCount=5  # 5MB
            ),
            logging.StreamHandler(sys.stdout),
        ],
    )

    # SQLAlchemy logger (adjust level as needed)
    sqlalchemy_logger = logging.getLogger("sqlalchemy")
    sqlalchemy_logger.setLevel(logging.WARNING)

    # Uvicorn access logger (disable if not needed)
    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.setLevel(logging.WARNING)

    # Return configured logger
    return logging.getLogger(__name__)
