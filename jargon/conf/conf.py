# Author: Justin gavin
# Description: This script will read all configuration files and build needed data structures


from jargon.conf import util_dict
from jargon.conf import util_keys


def get_command_word_dict():
    return util_dict.build_dict()


def get_keys_dict():
    return util_keys.build_dict()


