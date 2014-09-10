#!/usr/bin/env python

"""print function: 
   ,=space
   '\\'=\
   '\"'="
   \n = enter
   \t = tab
"""
print 'The quick brown fox','jumps over','the lazy dog\n'
print '1+200=',1+200,'\n'

#input 
name = raw_input('please enter your name:')
print 'hello','I\'m \"',name,'\"\n'
print '\\\\\\\t\\\\\\\\\n'
print r'\\\\\\\\t\\\\\\\\\'
print '\n'
print '''line1
line2
line3\n'''

#if,else
if (a=raw_input('enter an integer'))>=0:
	print a
else:
	print -a






