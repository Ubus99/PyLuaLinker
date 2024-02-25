import os
import sys


def import_global(module_name):
    globals()[module_name] = __import__(module_name)


sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))


import_global("src")
