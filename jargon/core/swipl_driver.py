# Author: Johan Burke

import subprocess
from threading import Thread
from queue import Queue, Empty

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)

def get_output(out_queue):
    out_str = ''
    try:
        while True:
            out_str += out_queue.get_nowait()
    except Empty:
        return out_str


def process_main():
    done = False
    i = 0

    goal_file = "prolog/test_kb.pl"

    while not done:
        prolog = subprocess.Popen(["swipl", goal_file], stdin = subprocess.PIPE, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell = True, universal_newlines = True, cwd = "jargon/core")
        #output = get_output(out_queue)
        #errors = get_output(err_queue)

        input_str = input()
        outdata, errdata = prolog.communicate(input_str)
        prolog.terminate()

        print("Output = " + outdata)
        outdata = outdata.split("=")
        varname, varval = outdata[0], outdata[1]
        print("varname: " + varname)
        print("varval: " + varval)
        print("Error = " + errdata)

        #print(output)
        #print(errors)

        #input_str = input()

        #prolog.stdin.write(input_str)
        i += 1
        if i == 2:
            done = True
