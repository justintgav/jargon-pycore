# Author: Johan Burke
# Text-based input driver which runs a REPL (Read-Eval-Print-Loop) loop

#from multiprocessing import Process, Pipe
# from ..core import swipl_driver
# import subprocess
from ..core import core

def driver_main(args):
    # swipl_driver.process_main(args)
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
    coreObj = core.Core(args)
    done = False
    while not done:
        user_input = input("> ")
        if "halt" in user_input:
            break
        print(coreObj.process_query(user_input))
