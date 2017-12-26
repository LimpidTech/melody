#!/usr/bin/env python

import os
import sys

from django.core import management

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melody.settings.development')

management.execute_from_command_line(sys.argv)
