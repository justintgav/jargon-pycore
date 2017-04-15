# Author: Johan Burke

import subprocess
import os.path
from time import sleep
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

# given a string like "Is it a thing?"
# return "[Is, it, a, thing]"
def as_prolog_list(input_str):
    return '[' + ','.join([x.strip('.?!,') for x in input_str.split(' ')]) + ']'

# construct a query from the given query_list
# query_list is a string returned by as_prolog_list
def construct_prolog_query(query_list):
    return 's(QueryType, {}, Leftovers).\n'.format(query_list)

def process_main(args):
    done = False
    i = 0

    wd = 'jargon/core'
    goal_file = "prolog/questions.pl"
    if args.verbose:
        print("------Goal file------")
        with open(os.path.join(wd, goal_file)) as f:
            for line in f:
                print(line)
        print("---------------------")

    # type "halt." to exit the loop
    while not done:
        prolog = subprocess.Popen(["swipl", goal_file], stdin = subprocess.PIPE, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell = False, cwd = wd) 

        input_str = as_prolog_list(input(">"))
        done = 'halt' in input_str

        if args.verbose:
            print('list str = ' + input_str)
        query = construct_prolog_query(input_str)
        if args.verbose:
            print('query = ' + query)
        sleep(0.25)
        outdata, errdata = prolog.communicate(query.encode())
        outdata = outdata.decode()
        errdata = errdata.decode()
        prolog.terminate()

        print("Output = " + outdata)
        outdata = outdata.split("\n")
        outdict = {}
        for line in outdata:
            key_val = line.split('=')
            if args.verbose:
                print(str(key_val))
            if len(line) > 1:
                outdict[key_val[0].strip(' ,')] = key_val[1].strip(' ,')
        print("Out dict:")
        print(str(outdict))
