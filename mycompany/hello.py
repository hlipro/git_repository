#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Hao Li'

import sys

def test():
	args = sys.argv
	# argv includes all command line parameters
	# argv[0] = the name of called module
	# E.g., python hello.py : argv[0] = hello.py
	if len(args) == 1:
		print 'Hello, world!'
	elif len(args) == 2:
		print 'Hello, %s!'%args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__': 
# if we call hello.py, python puts __name__ as __main__
# this can be used to debug the module
# as the following is only called when (python hello.py) or hello.test()
	test()
