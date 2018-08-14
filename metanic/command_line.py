import sys

from django.core import management


def execute():
    management.execute_from_command_line(sys.argv)
