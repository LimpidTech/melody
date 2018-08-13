#!/usr/bin/env python

import sys

from django.core import management


def execute_command_line():
    management.execute_from_command_line(sys.argv)


# We need this check to ensure we didn't import this from metanic, but that
# we are executing it as metanic's main entry.
if __name__ == '__main__':
    execute_from_command_line()
