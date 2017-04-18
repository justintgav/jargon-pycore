# Author: Justin Gavin
# Class to fake control of a light for demo purposes

class dummy_light:
    def on(self):
        print("The dummy light has been turned on!")

    def off(self):
        print("The dummy light has been turned off!")

    def white(self):
        print("The dummy light's color has been set to white!")

    def set_color(self, color):
        print("The dummy light's color has been set to " + str(color) + "!")

    def set_brightness(self, value):
        print("The dummy light's brightness has been set to " + str(value) + "!")
