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
	print 'Hi, %s, you have $%d.'%('Michael',100000)
	print '%2d-%02d'%(3,1)
	print '%.2f'%3.1415926
	    #can use %s for numbers
	print 'Age:%s. Gender: %s'%(25,True)
	    #unicode
	print u'Hi, %s'%u'Michael'
	print('growth rate: %d %%'%7)

a=raw_input('Need see encode module?(y/n): ')
if a=='y':
	#ASCII conversion
	print '%d'%(ord('A'))
	print '%s'%(chr(65))

	#unicode
	print u'中文'
	print u'中'

	#UTF-8 conversion
	print u'ABC'.encode('utf-8')
	print u'中文'.encode('utf-8')

	#decode into unicode
	print 'abc'.decode('utf-8')

a=raw_input('Need see data stucture module?(y/n): ')
if a=='y':
	print 'list'
	classmates=['Michael','Bob','Tracy']
	print len(classmates)
	print classmates[0]
	print classmates[1]
	print classmates[2]
	print classmates[-1]
	print classmates[-2]
	print classmates[-3]
	classmates.append('Adam') #add new element
	print classmates[-1]
	classmates.pop() #deletion of last element
	classmates.pop(1) #deletion of second element
	print classmates
	classmates[1]='Sarah'
	print classmates
	classmates.append(['asp','php'])
	print classmates
	print 'the length is %d'%len(classmates)











