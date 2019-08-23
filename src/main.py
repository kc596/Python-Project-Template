from src import utils

CONFIG = utils.get_config()
logger = utils.get_logger(__name__)

if __name__ == "__main__":
    logger.info("Project started!")
    print("Hello world!")
