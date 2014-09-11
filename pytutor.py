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
	print 'raw_input return string, NEED CONVERT TO INT'
	a=int(raw_input('enter an integer: '))
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
	print '\nlist'
	print  'sort(),replace(),pop(),append()'
	classmates=['Michael','Bob','Tracy']
	print 'the length is %d'%len(classmates)
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
	
	print '\ntuple'
	print 'tuple cannot change once defined: no append(), insert()'
	classmates=('Michael','Bob','Tracy',['php','asp'])
	print 'the length is %d'%len(classmates)
	print 'last element is %s'%classmates[-1]
	print 'first element is %s'%classmates[0]
	print 'We can change the list inside tuple'
	classmates[3][0]='python'
	classmates[3][1]='C++'
	print 'now the new last element is %s'%classmates[-1]

	print '\ndict:map-key'
	print 'key cannot be changed; can use tuple, cant use list'
	d = {'Michael':95,'Bob':75,'Tracy':85}
	print 'Grade of Michael: %d'%d['Michael']
	 #insert into dict
	d['Adam']=67;
	print 'Grade of Adam: %d'%d.get('Adam')
	 #delete key
	d.pop('Michael')
	print d

	print '\nset: set([a,b,c]); element must be different)'
	print 'add(key);remove(key);& (set intersect); | (set combine)'
	s = set([1, 1, 2, 2, 3, 3])
	print s
	s.add(4)
	print s
	s.remove(4)
	print s
	s1 = set([5,6,2])
	print '&:',s1&s
	print '|:',s1|s

a=raw_input('Need see if/for grammer module?(y/n): ')
if a=='y':
	print '\nif grammer: if, elif, else'
	age = 20
	print 'age=%d'%age
	if age >= 18:
	    print 'age>=18: adult'
	elif age >= 6:
	    print '18>age>=6: teenager'
	else:
	    print 'age<6: kid'
	
	print '\nfor grammer'
	names = ['Michael', 'Bob', 'Tracy']
	for name in names:
	    print name
	print 'compute sum of 0-100'
	print 'use function range(101) to generate 0-100'
	sum = 0
	for x in range(101):
	    sum = sum + x
	print sum
	print 'use while to compute sum of odd numbers in 0-100'
	sum = 0
	n = 99
	while n > 0:
	    sum = sum + n
	    n = n - 2
	print sum

a=raw_input('Need see function module?(y/n): ')
if a=='y':
	print 'common functions'
	print 'abs,cmp,int,float,bool,str,unicode'
	print 'function alias'
	a = abs
	print 'use alias to compute abs: %d'%a(-1)
	










