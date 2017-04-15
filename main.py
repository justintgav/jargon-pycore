# Author: Johan Burke

from jargon.driver import text_driver
import os

# TODO: insert logic to determine which driver to use
if __name__ == "__main__":
    print(os.getcwd())
    text_driver.main()
