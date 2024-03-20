import logging


class txtHandler(logging.Handler):

    def __init__(self):
        self.txt_saver = LogTxtSender()
        logging.Handler.__init__(self=self)
        self.addFilter(MyFilter())

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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "MyFilter": {
          "()": "filters_handlers_cust.MyFilter",
        }
    },
    "formatters": {
        "stdformatter": {"format": "%(asctime)s - %(levelname)s - %(module)s: line %(lineno)d - %(message)s",
                         "datefmt": "%d-%m-%Y %H:%M:%S"},
        },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "stdformatter",
            "filters": ["MyFilter"],
            'stream': 'ext://sys.stdout'
        },
        "fileHandler":{
            "class" : "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "stdformatter",
            "filename": "logs.log",
            "mode": "w",
            "encoding": "utf-8"
        },
        "txtHandler":{
            "class" : "filters_handlers_cust.txtHandler",
            "level": "INFO",
            "formatter": "stdformatter",
            "filters": ["MyFilter"]
        },
    },
    "loggers" : {
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

