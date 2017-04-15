# Author: Johan Burke
# Text-based input driver which runs a REPL (Read-Eval-Print-Loop) loop

#from multiprocessing import Process, Pipe
from ..core import swipl_driver
import subprocess

def driver_main(args):
    done = False
    swipl_driver.process_main(args)
    #parent_conn, child_conn = Pipe(True)
    #process = Process(target=swipl_driver.process_main, args=(child_conn,))
    #process.start()
    #while not done:
    #    print("$-", end="")
    #    s = input()
    #    #parent_conn.send(s)
    #    output = proc.communicate(s)
    #    print('Output from swipl: ')
    #    print(output)
