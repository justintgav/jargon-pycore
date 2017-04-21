# Author: Justin gavin
# Description: This script will read all configuration files and build needed data structures


from ..conf import util_dict
from ..conf import util_keys
from ..conf import util_ovr


def get_command_word_dict():
    return util_dict.build_dict()


def get_ovr_dict():
    return util_ovr.build_dict()


def get_keys_dict():
    return util_keys.build_dict()


