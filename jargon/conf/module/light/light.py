import ledcontroller

LIGHT_CONTROLLER_IP = "10.0.0.30"


def module_main(args):
    led = ledcontroller.LedController(LIGHT_CONTROLLER_IP)

    if "off" in args:
        led.off()
        return
    if "on" in args:
        led.on()
    if "white" in args:
        led.white()
    if "red" in args:
        led.set_color("orange")
        led.set_brightness(50)
    if "bright" in args:  # 'brighter' and 'brightness' also flags this
        if "brightness" in args:
            # assuming a numeric brightness level is specified, find it
            for i in str:
                if i.isdigit():
                    led.set_brightness(int(i))
                    return
        # if "brightness" not found, must be bright or brighter
        led.set_brightness(70)
        return
    if "dim" in args:
        led.set_brightness(30)
        return
