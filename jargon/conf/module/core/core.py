# Author: Justin Gavin
# Description: A module to handle simple basic responses (canned-responses and easter eggs for now)
#               In the future, storing and retrieving dynamic information should go here
#
# args format:
#   Either shove the entire query string in 'command'
#       or shove the dict phrase in 'command'
# Example NL Queries:
#   What is your name?
#       +args['command'] = 'your name'
#   >> I prefer to be called jargon
#
#   What is my name?
#    +args['command'] = 'my name'
#   >> You are a user, why would I care to know your name?
#
#   Thank you
#    +args['command'] = 'thank you'
#   >> You're welcome
#
#   Can entropy be reversed?
#    +args['command'] = 'entropy'
#   >> THERE IS AS YET INSUFFICIENT DATA FOR A MEANINGFUL ANSWER
#


# from random import randint


def module_main(args):
    command = args['command']
    if args['verbose']:
        print("Made it to core module")
        print("command content:\n" + command)
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
