# Author: Justin Gavin
# Description: A module to issue commands to a smartlight controller.
#               The IP of the controller should be specified in LIGHT_CONTROLLER_IP
#
# args format:
#   'command': must contain command phrase (Ex: 'on', 'off', 'red', 'brightness 70')
#              Can contain multiple commands in sequence:
#                   'on white brightness 70'
#              is a valid command and should be passed fully to this module
#               Passing the entire query to the module is valid.
#
# Example NL Queries:
#   Turn the lights on set them to red and the brightness to 50.
#    +args['command'] = 'on red brightness 50'
#   >> ##Action taken (or dummy printout), no actual response##
#
# Note: this has been converted for demo purposes, uses the dummy_light instead of
#           ledcontroller


# import ledcontroller
from jargon.conf.module.light import dummy_light

LIGHT_CONTROLLER_IP = "10.0.0.30"


def module_main(args):
    led = dummy_light.dummy_light()
    # led = ledcontroller.LedController(LIGHT_CONTROLLER_IP)
    if 'status' in args:
        command_string = args['status']
        if "off" in command_string:
            led.off()
            return
        if "on" in command_string:
            led.on()
    if 'brightness' in args:
        command_string = args['brightness']
        if command_string != 'default_brightness':
            led.set_brightness(command_string)
    if 'color' in args:
        command_string = args['color']
        if command_string != 'default_color':
            led.set_color(command_string)

    return ' '

    #if "off" in command_string:
    #    led.off()
    #    return
    #if "on" in command_string:
    #    led.on()
    #if "white" in command_string:
    #    led.white()
    #if "red" in command_string:
    #    led.set_color("orange")
    #    # led.set_brightness(50)
    #if "bright" in command_string:  # 'brighter' and 'brightness' also flags this
    #    if "brightness" in command_string:
    #        # assuming a numeric brightness level is specified, find it
    #        for i in command_string:
    #            if i.isdigit():
    #                led.set_brightness(int(i))
    #                return
    #    # if "brightness" not found, must be bright or brighter
    #    led.set_brightness(70)
    #    return
    #if "dim" in command_string:
    #    led.set_brightness(30)
    #    return
