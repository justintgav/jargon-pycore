# Author: Justin Gavin
# Description:  Read and build the command word dictionary
#               Will build dictionary from *.keys files in the module dir

import os


# master dictionary declaration
keys_dict = {}


# subroutine definitions
def __parse_dict_file(the_file):
    """Parse @param the_file"""
    input_file = open(the_file)
    module_name = input_file.next().strip()
    module_list = list()

    for line in input_file:
        module_list.append(line.strip())

    keys_dict[module_name] = module_list
    return


# returns a dictionary of all command words with associated program
def build_dict():
    dict_file_dir = './module/'

    for root, dirs, files in os.walk(dict_file_dir):
        for filename in files:
            if filename.endswith(".keys"):
                __parse_dict_file(root + "/" + filename)

    return keys_dict
