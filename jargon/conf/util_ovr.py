# Author: Justin Gavin
# Description:  Read and build the override word dictionary
#               Will build dictionary from *.ovr files in the module dir
#

import os


# master dictionary declaration
command_word_dict = {}


# subroutine definitions
def __parse_dict_file(the_file):
    """Parse @param the_file"""
    input_file = open(the_file)
    module_name = input_file.readline().strip()

    for line in input_file:
        command_word_dict[line.strip()] = module_name
    return


# returns a dictionary of all command words with associated module
def build_dict():
    dict_file_dir =  os.path.dirname(os.path.realpath(__file__)) + '/module/'
    #for filename in os.listdir(dict_file_dir):
    #    __parse_dict_file(dict_file_dir + filename)

    for root, dirs, files in os.walk(dict_file_dir):
        for filename in files:
            if filename.endswith(".ovr"):
                __parse_dict_file(root + "/" + filename)

    return command_word_dict
