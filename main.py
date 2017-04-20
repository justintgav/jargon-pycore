# Author: Johan Burke and Justin Gavin

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help = 'print more detailed debug information',
        action = 'store_true')
    parser.add_argument('-d', '--driver', type = str, choices = ['text_driver'],
        help = 'Select a driver to use.  If none is specified, defaults to text_driver', default = 'text_driver')
    return parser.parse_args()

def main():
    args = parse_args()
    exec("from jargon.driver import " + args.driver)
    exec(args.driver + ".driver_main(args)")

if __name__ == "__main__":
    main()
