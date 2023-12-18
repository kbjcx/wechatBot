import logging
import sys

def _reset_logger(logger):
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)
        del handler
    logger.hanlers.clear()
    logger.propogate = False # 关闭日志的继承
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        logging.Formatter("[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",)
    )
    
    file_handler = logging.FileHandler(filename="run.log", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",)
    )
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
def _get_logger():
    logger = logging.getLogger("wechat")
    _reset_logger(logger)
    logger.setLevel(logging.DEBUG)
    return logger

# logger
logger = _get_logger()