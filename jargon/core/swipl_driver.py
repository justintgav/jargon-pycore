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
    #out_queue = Queue()
    #err_queue = Queue()

    #out_thread = Thread(target = enqueue_output, args = (prolog.stdout, out_queue))
    #err_thread = Thread(target = enqueue_output, args = (prolog.stderr, out_queue))

    #out_thread.daemon = True
    #err_thread.daemon = True

    #out_thread.start()
    #err_thread.start()

    i = 0

    # TODO: this seems to work, just need to set up initial goals

    while not done:
        prolog = subprocess.Popen("swipl", stdin = subprocess.PIPE, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell = True, universal_newlines = True)
        #output = get_output(out_queue)
        #errors = get_output(err_queue)

        input_str = input()
        outdata, errdata = prolog.communicate(input_str)
        prolog.terminate()

        print("Output = " + outdata)
        print("Error = " + errdata)

        #print(output)
        #print(errors)

        #input_str = input()

        #prolog.stdin.write(input_str)
        i += 1
        if i == 2:
            done = True
