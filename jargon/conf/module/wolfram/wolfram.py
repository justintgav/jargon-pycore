# jtg's appid 5K8EHA-G654TY48VW
# https://pypi.python.org/pypi/wolframalpha

import wolframalpha


def module_main(args):
    client = wolframalpha.Client('5K8EHA-G654TY48VW')
    res = client.query(args)
    return next(res.results).text
