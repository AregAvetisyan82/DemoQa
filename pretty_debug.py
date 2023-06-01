import logging
from typing import Any

logger = logging.getLogger("Selenium_commands")

BLUE = "\033[34m"
BOLD = "\033[1m"
CYAN = "\033[36m"
ENDC = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
MAGENTA = "\033[35m"
UNDERLINE = "\033[4m"


def error_red(text: Any):
    logger.error(RED + f"{text}" + ENDC)


def warning_bold_red(text: Any):
    logger.warning(RED + BOLD + f"{text}" + ENDC + ENDC)


def info_light_blue(text: Any):
    logger.info(CYAN + f"{text}" + ENDC)
