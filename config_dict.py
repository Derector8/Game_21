import logging


class txtHandler(logging.Handler):
    """Custom handler for saving logs to .txt file"""

    def __init__(self):
        self.txt_saver = LogTxtSender()
        logging.Handler.__init__(self=self)

    def emit(self, record):
        self.txt_saver.write_log_to_txt(self.format(record))


class LogTxtSender:
    def __init__(self):
        pass

    def write_log_to_txt(self, msg):
        with open("all_logs.txt", 'a', encoding='utf-8') as file:
            file.write(f"{msg} \n")


class MyFilter(logging.Filter):
    """Filters messages, starting with 'Only_for_me' """

    def filter(self, record):
        return not record.getMessage().startswith('Only_for_me')


class LevelFilter(logging.Filter):
    """Filters messages with only WARNING or ERROR level to be recorded"""

    def filter(self, record):
        return (record.levelno == logging.WARNING or record.levelno == logging.ERROR)


class FuncNameFilter(logging.Filter):
    """Filters messages only from main module to be recorded """

    def filter(self, record):
        return record.module == 'main'


"""Config dict"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "MyFilter": {
            "()": "config_dict.MyFilter",
        },
        "LevelFilter": {
            "()": "config_dict.LevelFilter",
        },
        "FuncNameFilter": {
            "()": "config_dict.FuncNameFilter",
        }
    },
    "formatters": {
        "stdformatter": {"format": "%(asctime)s - %(levelname)s - %(module)s: line %(lineno)d - %(message)s",
                         "datefmt": "%d-%m-%Y %H:%M:%S"},
        "consoleformatter": {"format": "%(asctime)s - %(message)s",
                         "datefmt": "%H:%M:%S"},
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "consoleformatter",
            "filters": ["MyFilter"],
            'stream': 'ext://sys.stdout'
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "stdformatter",
            "filename": "logs.log",
            "mode": "w",
            "encoding": "utf-8",
            "filters": ["LevelFilter"]
        },
        "txtHandler": {
            "class": "config_dict.txtHandler",
            "level": "DEBUG",
            "formatter": "stdformatter",
            "filters": ["MyFilter", "FuncNameFilter"]
        },
    },
    "loggers": {
        "root": {
            "handlers": ["consoleHandler"],
            "level": "DEBUG",
        },
        "my_logging_hw": {
            "handlers": ["consoleHandler", "fileHandler", "txtHandler"],
            "level": "DEBUG"
        }
    }
}
