from bb_logger import logger
import logging


def test_common():
    logger.setup_logging(
        default_level=logging.INFO)
    logging.info('test common info', {'noti': True})


if __name__ == '__main__':
    test_common()
