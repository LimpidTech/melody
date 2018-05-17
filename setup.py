import setuptools
import sys


options = {}

if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    options['setup_requires'] = ['pytest-runner']


setuptools.setup(**options)
