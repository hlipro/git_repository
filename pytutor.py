#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=raw_input('Need see print module?(y/n): ')
if a=='y':
	"""print function: 
	   ,=space
	   '\\'=\
	   '\"'="
	   \n = enter
	   \t = tab
	"""
	print 'The quick brown fox','jumps over','the lazy dog'
	print '1+200=',1+200

	#input 
	name = raw_input('please enter your name:')
	print 'hello','I\'m \"',name
	print '\\\\\\\t\\\\\\\\'
	print r'\\\\\\\\t\\\\\\\\'
	print '''line1
	line2
	line3'''

	#if,else
	a=raw_input('enter an integer: ')
	if a>=0:
		print a
	else:
		print -a
    #print format
    # %s: sting, %d:integer, %f:float, %x:hex
    'Hi, %s, you have $%d.'%('Michael',100000)
    '%2d-%02d'%(3,1)
    '%.2f'%3.1415926
    #can use %s for numbers
    'Age:%s. Gender: %s'%(25,True)
    #unicode
    u'Hi, %s'%u'Michael'
    print('growth rate: %d %%'%7)
    
a=raw_input('Need see encode module?(y/n): ')
if a=='y'
	#ASCII conversion
	ord('A')
	chr(65)

	#unicode
	print u'中文'
	u'中'

	#UTF-8 conversion
	u'ABC'.encode('utf-8')
	u'中文'.encode('utf-8')

	#decode into unicode
	'abc'.decode('utf-8')









