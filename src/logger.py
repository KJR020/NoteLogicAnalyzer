import logging


def setup_logger(name, log_file, level=logging.INFO):
    """ロガーを設定する関数"""
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s %(message)s")
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
