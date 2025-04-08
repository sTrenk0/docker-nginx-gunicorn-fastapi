from .setup import get_configured_app
from .logger import setup_logger


setup_logger()
app = get_configured_app()

