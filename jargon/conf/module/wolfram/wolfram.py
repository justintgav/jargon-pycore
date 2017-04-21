# Author: Justin Gavin
# Description: A module to query wolfram alpha.
#               Wolfram Alpha can handle anything, somewhat overpowered.
#               Due to this, you explicitly have to use "wolfram" or "math" in jargon command
#
# args format:
#   'command': the entire meaningful command
#
# Example NL Queries:
#   What is 5+5?
#    +args['command'] = '5+5'
#   >> 10
#
# jtg's appid 5K8EHA-G654TY48VW
# https://pypi.python.org/pypi/wolframalpha

import wolframalpha


def module_main(args):
    client = wolframalpha.Client('5K8EHA-G654TY48VW')
    res = client.query(args['query'])
    try:
        return next(res.results).text
    except AttributeError:
        pass

# Example use
# print(module_main({'command': '5+5'}))