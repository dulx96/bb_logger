from bb_logger import logger
import logging
LOG = logging.getLogger(__name__)


def test_common():
    logger.setup_logging(default_level=logging.INFO)
    LOG.info('test common info', noti=True)
