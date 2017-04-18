# Author: Justin Gavin
# Description: A module to query wolfram alpha.
#               Wolfram Alpha can handle anything, somewhat overpowered.
#               Due to this, you explicitly have to use "wolfram" or "math" in jargon command
#
# jtg's appid 5K8EHA-G654TY48VW
# https://pypi.python.org/pypi/wolframalpha

import wolframalpha


def module_main(args):
    client = wolframalpha.Client('5K8EHA-G654TY48VW')
    res = client.query(args['command'])
    return next(res.results).text

# Example use
# print(module_main({'command': '5+5'}))