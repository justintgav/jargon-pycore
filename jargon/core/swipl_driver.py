# Author: Johan Burke

import subprocess
import os
import os.path
from time import sleep
from ..conf import conf

#from threading import Thread
#from queue import Queue, Empty

#def enqueue_output(out, queue):
#    for line in iter(out.readline, b''):
#        queue.put(line)
#
#def get_output(out_queue):
#    out_str = ''
#    try:
#        while True:
#            out_str += out_queue.get_nowait()
#    except Empty:
#        return out_str

# prolog fusses if we use strings like '5pm'
# so add quotes if the first character is a digit
def quote_if_necessary(x):
    result = x
    if x[0].isdigit():
        result = "'" + result + "'"
    return result

# given a string like "Is it a thing?"
# return "[Is, it, a, thing]"
def as_prolog_list(input_str):
    return '[' + ','.join([quote_if_necessary(x.strip('.?!,').lower()) for x in input_str.split(' ')]) + ']'

# construct a query from the given query_list
# query_list is a string returned by as_prolog_list
def construct_prolog_query(query_list):
    return 's(Param1, Param2, Param3, QueryType, {}, []).\n'.format(query_list)

def get_module_name(query_type):
    return query_type[:-len("_query")]

def map_params(key_list, arg_dict):
    result = {}
    for i in range(len(key_list)):
        result[key_list[i]] = arg_dict['Param' + str(i + 1)]
    return result

def process_main(args):
    done = False
    i = 0

    # Step 1: load up all grammar files
    wd = 'jargon/conf'
    goals = []
    for subdir, _, files in os.walk(wd):
        goals.extend([os.path.join(subdir, filename) for filename in files if filename.endswith('.pl')])
    if args.verbose:
        print("Goal files:")
        for filename in goals:
            with open(filename) as f:
                print("---------------")
                for line in f:
                    print(line)
                print("---------------")

    os.chdir(wd)
    module_keys_dict = conf.get_keys_dict()
    if args.verbose:
        print("Module keys dictionary:")
        print(str(module_keys_dict))
    os.chdir('../..')

    # Step 2: get user input
    # either the string 'halt.' or some type of query
    cl_args = ["swipl"]
    cl_args.extend(goals)
    while not done:
        prolog = subprocess.Popen(cl_args, stdin = subprocess.PIPE, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell = False) 

        input_str = input("> ")
        if input_str.strip() == 'halt.':
            done = True
        else:
            # Step 3: convert the user's English sentence into
            # a list of words to be parsed by Prolog
            input_str = as_prolog_list(input_str)

            if args.verbose:
                print('list str = ' + input_str)
            query = construct_prolog_query(input_str)
            if args.verbose:
                print('query = ' + query)
            sleep(0.25)

            # Step 4: pass the user's query to prolog
            outdata, errdata = prolog.communicate(query.encode())
            outdata = outdata.decode()
            errdata = errdata.decode()
            prolog.terminate()

            # Step 5: process the prolog results into data structures
            print("Output = ")
            print(outdata)
            if args.verbose:
                print("Error = " + errdata)
            outdata = outdata.split("\n")
            outdict = {}
            for line in outdata:
                key_val = line.split('=')
                if args.verbose:
                    print(str(key_val))
                if len(line) > 1:
                    outdict[key_val[0].strip().strip(',')] = key_val[1].strip().strip(',')
            module_name = get_module_name(outdict['QueryType'])
            if args.verbose:
                print("Out dict:")
                print(str(outdict))
                print("Selected module: " + module_name)
            params_dict = map_params(module_keys_dict[module_name], outdict)
            if args.verbose:
                print("Param dict:")
                print(str(params_dict))
            import_statement = "from ..conf.module.{0} import {0}".format(module_name)
            if args.verbose:
                print("Code to run:")
                print(import_statement)
            exec(import_statement)
            main_statement = "{0}.module_main(params_dict)".format(module_name)
            if args.verbose:
                print("Code to run:")
                print(main_statement)
            output_str = eval(main_statement)
            print(output_str)
