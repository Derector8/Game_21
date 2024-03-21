import logging.config
from logging.config import dictConfig
import config_dict

dictConfig(config_dict.LOGGING)
logger_1 = logging.getLogger('my_logging_hw')


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
