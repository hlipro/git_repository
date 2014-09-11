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
	print 'single element tuple (1,):',(1,)

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
	print 'use alias a(-1) to compute abs(-1): %d'%a(-1)
	print '\nnow def functions'
	#here raise is for error reporting
	#E.g. raise Exception('error')
	def my_abs(x):
		if not isinstance(x,(int,float)):
			raise TypeError('bad operand type')
		if x>=0:
			return x
		else:
			return -x
	print 'try my_abs'
	a = float(raw_input('give me some number: '))
	print 'its abs is: %f'%my_abs(a)

	print '\ntry multiple return (actually return is a tuple)'
	import math
	def move_pt(x,y,step,angle=0):
		nx = x+step*math.cos(angle)
		ny = y-step*math.sin(angle)
		return nx, ny
	nx, ny = move_pt(100,100,10,math.pi/3)
	print 'Multiple returns: nx = %f, ny = %f'%(nx,ny)

	print '\ndefault argument'
	def my_power(x,n=2):
		s = 1
		while n>0:
			s=s*x
			n=n-1
		return s
	print 'my_power(2)=4 ?: ',my_power(2)==4
	print 'my_power(2,3)=8 ?: ',my_power(2,3)==8

	print '\ntrap in default argument'
	def my_append(L=[]):
		L.append('end')
		return L
	print 'now try to add append with my_append'
	print my_append()
	print my_append()
	print my_append()
	print 'something wrong'
	print '\ntry my_new_append'
	def my_new_append(L=None):
		if L==None:
			L = []
		L.append('end')
		return L
	print my_new_append()
	print my_new_append()
	print my_new_append()
	print 'bug fixed'

	print '\nvarying argument: use * ahead of argument'
	def calc_sum_square(*numbers):
		sum = 0
		for n in numbers:
			sum = sum + n*n
		return sum
	print 'square sum of 1-3: ', calc_sum_square(1,2,3)
	print 'square sum of a list: ', calc_sum_square(*range(4))

	print '\nkey word argument: **'
	def my_staff(name,age,**kw):
		print 'name:',name,'age:',age,'other:',kw
	my_staff('Bob',35,city='Beijing')
	kw = {'city':'Beijing','job':'Engineer'}
	my_staff('Jack',24,**kw)

	print '\nfor function argument, the order is'
	print 'necessary, default, varying, keyword'
	print 'example'
	def my_func(a,b,c=0,*args,**kw):
		print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
	print 'try my_func'
	args = (1,2,3,4,5,6)
	kw = {'age':15,'job':'student'}
	my_func(*args,**kw)

	print '\nrecursive function'
	def my_fact(n):
		if n == 1:
			return 1
		return n*my_fact(n-1)
	print '10! =',my_fact(10)
	print 'simple, but not optimized!'

	print '\nrecursive w/ tail optimized'
	print '''return function itself;\ncannot 
	contain an expression of that function'''
	def my_fact_new(n):
		return fact_iter(1,1,n)
	def fact_iter(product,count,max):
		if count>max:
			return product
		return fact_iter(product*count,count+1,max)
	print '100! =',my_fact_new(100)

a=raw_input('Need see advanced function module?(y/n): ')
if a=='y':
	print '\nslice'
	L = range(20)
	print L[0:3] #get the first three: from 0 to 2
	print L[:3]
	print L[1:3] #get the second and third: from 1 to 2
	print L[-2:] #get -2 and -1
	print L[-2:-1] #get -2
	print L[:10]
	print L[-10:]
	print L[:10:2]
	print L[::5] #get one every 5
	print L[:] #list all
	print (0,1,2,3,4,5)[:3] #first 3 of a tuple
	print 'ABCDEFG'[:3] #first 3 of a string

	print '\niteration'
	print 'iteration in dict'
	d = {'a':1,'b':2,'c':3}
	print 'key in d'
	for key in d:
		print key
	print 'value in d'
	for value in d.itervalues():
		print value
	print 'both key and value in d'
	for key,value in d.iteritems():
		print key,value
	print 'iteration in string'
	for ch in 'ABCDEFG':
		print ch
	print 'to know whether target is iterable'
	print 'use isinstance(\'\',Iterable) from collections'
	from collections import Iterable
	print isinstance('abc',Iterable) 
	print isinstance(1213,Iterable)
	print 'use enumerate to change list into key-map'
	for i,value in enumerate(['A','C','D']):
		print i,value
	for x,y in [(1,1),(2,4),(3,9)]:
		print x,y

	print '\nlist comprehensions'
	print [x*x for x in range(1,11)]
	print [x*x for x in range(1,11) if x%2 ==0]
	print 'two levels'
	print [x*x + y*y for x in range(1,5) for y in range(6,10)]
	print 'list all directories & files'
	import os
	print [di for di in os.listdir('.')]
	print [k + '=' + str(v) for k,v in d.iteritems()]

	print '''\ngenerator: to save space or for infinite many elements, only generate current item'
	function: next(),yield'''
	g = (x*x for x in range(10))
	print g.next()
	print 'use \'for\' to iterate'
	for n in g:
		print n
	print 'def generator function'
	def fib(max):
		n,a,b = 0,0,1
		while n<max:
			yield b
			a,b = b, a+b #simultaneous value pass
			n = n+1
	print 'everytime the function is called, it return at yield.\n\
	and for the next time it\'s called, it begins at yield'
	for n in fib(10):
		print n

a=raw_input('Need see higher-order functional programming module?(y/n): ')
if a=='y':
	print 'map(func,list):pass every element in list to func'
	def f(x):
		return x*x
	print map(f,range(1,10))
	print 'reduce(func,list):func(func(func(x1,x2),x3),x4)...'
	def add(a,b):
		return a+b
	reduce(add,[x for x in range(1,10) if x%2 == 1])
	print 'example'
	def fn(x,y):
		return 10*x+y
	print reduce(fn,[1,3,5,7,9])
	print reduce(fn,map(int,'13579'))#take in a string, convert to number
	def str2int(s):
		def fn(x,y):
			return 10*x+y
		return reduce(fn,map(int,s))
	print '\nhigher-order sort'
	print 'example 1: reverse sort'
	print sorted([36,5,12,9,21])
	def reversed_cmp(x,y):
		if x>y:
			return -1 #normal return 1
		if x<y:
			return 1
		return 0
	print sorted([36,5,12,9,21],reversed_cmp)
	print 'example 2: ignore string case'
	def cmp_ignore_case(s1,s2):
		u1 = s1.upper()
		u2 = s2.upper()
		if u1<u2:
			return -1
		if u1>u2:
			return 1
		return 0
	print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)

	print '\nreturn function'
	def lazy_sum(*args):
		def sum():
			ax = 0;
			for n in args:
				ax = ax + int(n)
			return ax
		return sum
	f1 = lazy_sum(*[1,3,4,7,9])
	print f1()

	print '\nanonymous function: lambda, only for simple case'
	print 'example'
	print map(lambda x: x*x, [1 ,2 ,3 ,4, 5, 6])

	print '\ndecorator'
	print 'first example: two layers'
	def log(func):
		def wrapper(*args,**kw):
			print 'call %s():'%func.__name__
			return func(*args,**kw)
		return wrapper
	@log
	def now():
		print '2014-09-11'
	print 'try to call now():'
	print 'step 1: call log(func(*,**))->return wrapper(*,**)'
	print 'step 2: call wrapper(*,**)->print and call func(*,**)'
	now()
	print '\nsecond example: three layers'
	def log(text):
		def decorator(func):
			def wrapper(*args,**kw):
				print '%s %s(): '%(text,func.__name__)
				return func(*args,**kw) 
				#note: here returned value=function(*,**); try to call func
			return wrapper 
			#note: here returned function
		return decorator
	@log('execute')
	def now():
		print '2014-09-11'
	print 'try to call now()'
	print 'step 1: call log(text)(func(*,**))-> return decorator(func(*,**))'
	print 'step 2: call decorator(func(*,**))-> return wrapper(*,**)'
	print 'step 3: call wrapper(*,**)-> return print and func(*,**)'
	now()
	print '\nproblem: now.__name__ = %s'%now.__name__
	print 'bug fix'
	import functools
	def log(text):
		def decorator(func):
			print 'save func.__name__ here'
			@functools.wraps(func) #save func.__name__
			def wrapper(*args,**kw):
				print '%s %s(): '%(text,func.__name__)
				return func(*args,**kw)
			return wrapper
		return decorator
	@log('excecute')
	def now():
		print '2014-09-11'
	print 'now.__name__ = %s'%now.__name__
	print '\n third example'
	def log(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'begin call'
			func(*args,**kw)
			print 'end call'
			def f_nothing(*args1,**kw1):
				pass
			return f_nothing(*args,**kw)
		return wrapper
	@log
	def now():
		print '2014-09-11'
	print 'call now():'
	now()
	print '\n fourth example: default argument in decorator'
	def log(text=None):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				if text == None:
					print 'call %s: '%func.__name__
					return func(*args,**kw)
				print '%s %s: '%(text,func.__name__)
				return func(*args,**kw)
			return wrapper
		return decorator
	@log
	def now():
		print '2014-09-11'
	now()

	print '\npartial function'
	int2 = functools.partial(int,base=2)
	print int2('1000000')
	print int2('1000000',base=10) #we can also reset the base


a=raw_input('Need see module module?(y/n): ')
if a=='y':
	print 'setup library'
	print 'use shell command: sudo easy_install ***'
	print 'E.g., sudo pip uninstall PIL ; brew install libjpeg ; sudo easy_install PIL'
	print 'usefull libs: pip, MySQL-python,', 'numpy (numerical computation),', 'Jinja2 (text)'
	print 'example of using PIL'
	import Image
	im = Image.open('/Users/haoli/Downloads/OneDrive/Pictures/Saved pictures/IMG_1044_JPG.jpg')
	print im.format, im.size, im.mode
	im.save('thumb.png')
	im = Image.open('thumb.png')
	im.thumbnail((200,100)) #resize, not working for jpeg?
	im.save('thumb.jpg','JPEG')
	import os
	os.remove('thumb.jpg')
	os.remove('thumb.png')
	#os.rmdir() : rmdir
	#shutil.rmtree() : rm directory and all its contents
	print '\n setup module path'
	import sys
	sys.path.append('/Users/haoli/developer/git_repository')
	# or use PYTHONPATH = '/User/ ...' 

	print '\n__future__: to test current code on future python versions'
	print 'usage: from __future__ import unicode_literals (or division)'
	print 'in python 3.*: all \'xxx\' is unicode, rather string.\
	string is b\'xxx\''
	print 'in python 2.7: 10/3 = 3 (floor over), 10.0/3 = 3.33333'
	print 'in python 3.*: 10/3 = 3.33333, 10//3 = 3'
	
















































