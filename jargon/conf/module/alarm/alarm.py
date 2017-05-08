import ledcontroller, threading, time
from datetime import datetime, timedelta

LIGHT_CONTROLLER_IP = "10.0.0.30"
led = ledcontroller.LedController(LIGHT_CONTROLLER_IP)


def light_on():
    led.on()


def module_main(args):
    query = args['query']

    #5 seconds
    t = threading.Timer(query, light_on, ())
    t.start()
    return "alarm sched"

if __name__ == "__main__":
    args_dict = {}

    user_in = input("> ").split(':')


    #https://stackoverflow.com/questions/36810003/python-calculate-seconds-from-now-to-specified-time-today-or-tomorrow
    now = datetime.now()
    args_dict['query'] = (timedelta(hours=24) - (now - now.replace(hour=int(user_in[0]), minute=int(user_in[1]), second=0, microsecond=0))).total_seconds() % (24 * 3600)

    print(module_main(args_dict))
