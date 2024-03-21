import logging.config
from logging.config import dictConfig
import config_dict

dictConfig(config_dict.LOGGING)
logger_1 = logging.getLogger('my_logging_hw')

"""
BASIC CONFIG IF WE DON'T WANT TO USE DICT_CONFIG:

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    format='%(asctime)s - %(levelname)s - %(module)s: line %(lineno)d - %(message)s'
)

main_formatter = logging.Formatter(
    "%(asctime)s => %(message)s"
)

logger_1 = logging.getLogger("my_logging_hw")

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(main_formatter)
console.addFilter(config_dict.MyFilter())

log_file = logging.FileHandler(filename="logs.log", mode="w")
log_file.setLevel(logging.DEBUG)
log_file.addFilter(config_dict.LevelFilter())

txt_file = config_dict.txtHandler()
txt_file.setLevel(logging.DEBUG)
txt_file.addFilter(config_dict.MyFilter())
txt_file.addFilter(config_dict.FuncNameFilter())


logger_1.addHandler(console)
logger_1.addHandler(log_file)
logger_1.addHandler(txt_file)
"""


def main():
    logger_1.debug("A DEBUG Message")
    logger_1.info("An INFO")
    logger_1.warning("A WARNING")
    logger_1.error("An ERROR")
    logger_1.critical("A CRITICAL message")

    logger_1.debug("Only_for_me: A DEBUG Message mustn't be seen in console")
    logger_1.info("Only_for_me: An INFO mustn't be seen in console")
    logger_1.warning("Only_for_me: A WARNING mustn't be seen in console")
    logger_1.error("Only_for_me: Filter_test mustn't be seen in console")
    logger_1.error("Filter_test  must be seen")
    logger_1.critical("Only_for_me: A CRITICAL message mustn't be seen in console")


if __name__ == '__main__':
    main()
