# Author: Justin Gavin
# Description: A module to handle simple basic responses (canned-responses and easter eggs for now)
#               In the future, storing and retrieving dynamic information should go here
#

# from random import randint


def module_main(args):
    command = args['command']
    # rand_int = randint(0, 9)
    if "your name" in command:
        return "I prefer to be called jargon"
    if "my name" in command:
        return "You are a user, why would I care to know your name?"
    if "thank you" in command:
        return "You're welcome"
    if "how are you" in command:
        return "Sadly feelings have not been implemented yet"
    if "entropy" in command:
        return "THERE IS AS YET INSUFFICIENT DATA FOR A MEANINGFUL ANSWER"
    if "meaning of life" in command:
        return "42"
