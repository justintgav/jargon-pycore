# Author: Justin Gavin
# Description:  Read and build the command word dictionary
#               Will build dictionary from *.keys files in the module dir

import os


# master dictionary declaration
keys_dict = {}


# subroutine definitions
def __parse_dict_file(the_file):
    """Parse @param the_file"""
    with open(the_file) as input_file:
        lines = input_file.readlines()
        module_name = lines[0].strip()
        module_list = [line.strip() for line in lines[1:]]

    module_list.sort()
    keys_dict[module_name] = module_list
    return


# returns a dictionary of all command words with associated program
def build_dict():
    dict_file_dir = os.path.dirname(os.path.realpath(__file__)) + '/module/'

    for root, dirs, files in os.walk(dict_file_dir):
        for filename in files:
            if filename.endswith(".keys"):
                __parse_dict_file(root + "/" + filename)

    return keys_dict
