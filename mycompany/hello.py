#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Hao Li'

import sys
# use alias to import module
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO
try:
	import json # python >=2.6
except ImportError:
	import simplejson as json # python < 2.6

# private functions/variables are defined by adding _ or __ ahead of name
# private functions are only used inside module to pack sourse codes
# public functions are open, and could call private functions
def _private_1():
	print 'Hello, world!'
def _private_2(args):
	print 'Hello, %s!'%args[1]

def test():
	args = sys.argv
	# argv includes all command line parameters
	# argv[0] = the name of called module
	# E.g., python hello.py : argv[0] = hello.py
	if len(args) == 1:
		_private_1()
	elif len(args) == 2:
		_private_2(args)
	else:
		print 'Too many arguments!'

if __name__ == '__main__': 
# if we call hello.py, python puts __name__ as __main__
# this can be used to debug the module
# as the following is only called when (python hello.py) or hello.test()
	test()
