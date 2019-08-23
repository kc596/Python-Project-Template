import copy
import logging
import logging.config
import os
import yaml
from src import constants


INIT = False
LOGGER_INITIALIZED = False
CONFIG = None
CONFIG_FILE_NAME = constants.CONFIG_FILE_NAME
CONFIG_FILE_PATH = os.environ[constants.ENV_VAR_CONFIG_PATH]
PROFILE = os.environ[constants.ENV_VAR_PROFILE]


def get_config():
    global CONFIG
    if CONFIG is None:
        configfile = "{}/{}.yaml".format(CONFIG_FILE_PATH, CONFIG_FILE_NAME)                    # general config
        with open(configfile, 'r') as cf:
            CONFIG = yaml.safe_load(cf.read())
        if len(PROFILE) > 0:
            configfile = "{}/{}-{}.yaml".format(CONFIG_FILE_PATH, CONFIG_FILE_NAME, PROFILE)    # environment config
            with open(configfile, 'r') as cf:
                merge_dict(CONFIG, yaml.safe_load(cf.read()))
    return copy.deepcopy(CONFIG)


def merge_dict(original_dict, new_dict):
    """Populate original_config from new_config keeping disjoint properties from original_config"""
    if type(new_dict) is not dict:
        return
    for key in new_dict.keys():
        if type(new_dict[key]) is dict:
            if key in original_dict.keys() and type(original_dict[key]) is dict:
                merge_dict(original_dict[key], new_dict[key])
            else:
                original_dict[key] = new_dict[key]
        else:
            original_dict[key] = new_dict[key]


def get_logger(name):
    if LOGGER_INITIALIZED is False:
        initialize_logger()
    logger = logging.getLogger(name)
    return logger


def initialize_logger():
    global LOGGER_INITIALIZED
    if CONFIG is None:
        get_config()
    create_log_directory()
    logging.config.dictConfig(CONFIG['logs'])
    LOGGER_INITIALIZED = True
    logger = logging.getLogger(__name__)
    logger.info("Logger initialized!")
    logger.info("Using profile: {}".format(PROFILE))


def create_log_directory():
    os.makedirs(os.path.dirname(str(CONFIG['logs']['handlers']['file']['filename'])), exist_ok=True)
