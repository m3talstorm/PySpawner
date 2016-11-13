"""
"""

# Native
import os
import time
import argparse
import multiprocessing
import importlib

# 3rd-Party

# Proprietary


# Guard against imports
if not (__name__ == '__main__'):
    sys.exit(0)


__VERSION__ = '0.0.1'


def spawn(path):
    # Work out the module that should be imported
    module = importlib.import_module(path)

    return None


# Arguments
parser = argparse.ArgumentParser(description='PySpawner')

parser.add_argument('--module', action='store', default=None)
parser.add_argument('--count', action='store', default=5)

args = parser.parse_args()

if not args.spawn:
    raise Exception("No spawn specified")

spawns = []

for i in xrange(int(args.count)):

    spawned = multiprocessing.Process(target=spawn, args=(args.module,))

    spawns.append(spawned)
    spawned.start()
