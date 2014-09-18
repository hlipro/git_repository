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

a=raw_input('Need see OOP module?(y/n): ')
if a=='y':
	class Student(object): 
	# object is where the class inherits from
	# keep properties private by adding __
		def __init__(self, name, score): #initialization
			self.__name = name
			self.__score = score

		def print_score(self):
			print '%s: %s' % (self.__name, self.__score)

		def get_grade(self):
			if self.__score >= 90:
				return 'A'
			elif self.__score>= 60:
				return 'B'
			else:
				return 'C'

		def set_score(self,score):
			if 0<= score <= 100:
				self.__score = score
			else:
				raise ValueError('bad score')

		def get_score(self):
			return self.__score

	bart = Student('Bart Simpson', 59)
	lisa = Student('Lisa Simpson', 87)
	bart.print_score()
	lisa.print_score()
	bart.get_grade()
	bart.get_score()
	print 'in class, private function __***__ and private var __** cannot be visited from outside'

	print '\nclass inheritation'
	class Animal(object):
		def run(self):
			print 'Animal is running...'

	class Dog(Animal):
		def run(self): # function re-def
			print 'Dog is running...'

	class Cat(Animal):
		def run(self): # function re-def
			print 'Cat is running...'

	print 'polymorphism: any function defined for father class can adapt to daughter classes'
	def run_twice(animal):
		animal.run()
		animal.run()

	run_twice(Dog())
	run_twice(Cat())	

	print '\nobtain object information: type(),isinstance(),dir()'
	import types
	print type('abc')==types.StringType
	print type(u'abs')==types.UnicodeType
	print type([])==types.ListType
	print type(int)==type(str)==types.TypeType

	a = Animal()
	b = Dog()
	print isinstance(b,Animal)
	print isinstance(b,Dog)
	print isinstance(a,Dog)
	print isinstance(u'a',(str,unicode))

	print dir('ABC') #return all properties and methods
	print 'ABC'.__len__() # not good to call private function

	class MyObject(object):
		def __init__(self):
			self.x=9
		def power(self):
			return self.x*self.x

	obj = MyObject()
	if hasattr(obj,'x'): # is there a property 'x'?
		print obj.x
	if not hasattr(obj,'y'):
		setattr(obj,'y',19)
	if hasattr(obj,'y'):
		print getattr(obj,'y')
	print getattr(obj,'z',404) # 404 not found
	print hasattr(obj,'power')
	fn = getattr(obj,'power')
	print '%d\n'%fn()

a=raw_input('Need see advanced OOP module?(y/n): ')
if a=='y':
	print 'We can change property/func of an instance/class'
	class Student(object):
		pass

	s = Student()
	print 'add a property'
	s.name = 'Michael'
	print s.name
	print 'add a function to an instance'
	from types import MethodType
	def set_age(self,age):
		self.age = age
	s.set_age = MethodType(set_age,s,Student)
	s.set_age(25)
	print s.age

	print 'add a function to a class'
	Student.set_age = MethodType(set_age,None,Student)
	s1 = Student()
	s1.set_age(20)
	print s1.age

	print 'if we want to restrict changes to a class, use __slots__'
	class Student(object):
		__slots__ = ('name','age') #use tuple for __slots__

	s = Student()
	s.name = 'Michael'
	s.age = 25
	#s.score = 99 # not allowed to do this
	print 'for daughter class, it will not inherit __slots__ if not defined'
	class BlackStudent(Student):
		pass
	g = BlackStudent()
	g.score = 100
	print g.score # this is allowed since __slots__ not inherited

	class WhiteStudent(Student):
		__slots__ = ('gender')
	g = WhiteStudent()
	#g.score = 100 # not allowed

	print '\n@property decorator converts a getter func into a property'
	class Student(object):

		@property
		def score(self):
		    return self.__score
		@score.setter
		def score(self, value):
			if not isinstance(value,int):
				raise ValueError('input value must be an integer!')
			if value <0 or value > 100:
				raise ValueError('input value must be within [0, 100]')
			self.__score = value

		@property
		def lost_pt(self):
			return 100 - self.__score

	print 'now we can use score as property:'
	s=Student()
	s.score = 60 # call score.setter to set score
	print 'his score is: %d'%s.score # call score getter to get score
	print 'he lost %d points'%s.lost_pt # this is also a property, and a func

	print '\nmultiple inheritance'
	class Animal(object):
		pass
	class Mammal(Animal):
		pass
	class RunnableMixin(object):
		def run(self):
			print 'Running...'
	class Dog(Mammal, RunnableMixin):
		pass

	print '\nspecial vars/funcs: __slots__,__len__(),__str__,__repr__'
	class Student(object):
		def __init__(self,name=None):
			self.__name = name
		def __str__(self):
			return 'Student object (name=%s)'%self.__name
		__repr__ = __str__
	print Student('Hao')

	print 'special: __iter__(), next() used in interation;\
	 __getitem__(),__setitem__(),__delitem__() makes class like list/dict'
	class Fib(object):
		def __init__(self):
			self.a, self.b = 0, 1
		def __iter__(self):
			return self
		def next(self):
			self.a,self.b=self.b,self.a+self.b
			if self.a>10:
				raise StopIteration()
			return self.a
		def __getitem__(self,n): # so we can call Fib()[i], i could be slice
			if isinstance(n,int):
				a,b = 1,1
				for x in range(n):
					a,b = b,a+b
				return a
			if isinstance(n,slice):
				start = n.start
				stop = n.stop
				L = []
				a,b = 1, 1
				for x in range(stop):
					a,b = b,a+b
					if x>= start:
						L.append(a)
				return L

	for n in Fib():
		print n

	for n in range(10):
		print 'nth element is:', Fib()[n]
	#	__setitem__(): set value to class as a list/dict
	#   __delitem__(): del element of class as list/dict

	print 'special: __getattr__(): dynamic return a property that\' not defined in class'
	class Student(object):

		def __init__(self):
			self.name = 'Michael'

		def __getattr__(self, attr): # define other properties here
			if attr=='score':
				return 99
			if attr=='age': # can also return a func
				return lambda: 25
			raise AttributeError('\'Student\' object has no attribute \'%s\''%attr)
			# for attr not in this func, still return an error

	s = Student()
	print s.name
	print s.score
	print s.age() #since s.age returns a function, need call s.age() for value
	print 'dynamic path generation by __getattr__'
	class Chain(object):
		def __init__(self,path=''):
			self._path = path
		def __getattr__(self,path):
			return Chain('%s/%s'%(self._path,path))
		def __str__(self):
			return self._path
	print Chain().status.user.timeline.list

	print 'dynamic path with user name'
	class Chain(object):
		def __init__(self,path='Users'):
			self._path = path
		def users(self,name):
			return Chain('%s/%s'%(self._path, name))
		def __getattr__(self,path):
			return Chain('%s/%s'%(self._path,path))
		def __str__(self):
			return self._path
	print Chain().users('hlipro').developer.git_repository

	print '__call__(): define instance(): e.g. s= Student();\
	s() defined by s.__call__()'
	class Student(object):
		def __init__(self,name='Hao'):
			self.name = name
		def __call__(self,name):
			print 'Hi, %s, my name is %s.'% (name,self.name)

	s = Student('Hao')
	s('Michael') # call __call__()

	print 'can use callable to see whether object is callable'
	print 'is Student() (an instance) callable? %s'%callable(Student())

	print '\nuse type() to create dynamic class'	
	def fn(name='world'):
		print 'Hello, %s'%name
	Hello = type('Hello',(object,),dict(hello=fn)) #create a Hello class
	print type(Hello)
	h = Hello()
	print type(h)
	h.hello()

	print '\nmetaclass -> create class -> create instance'
	class listMetaclass(type):
		def __new__(cls,name,bases,attrs):
			# class object, class name, class father, class func-name dictionary
			attrs['add'] = lambda self, value: self.append(value)
			return type.__new__(cls,name,bases,attrs)
			# return a new class with modified attrs

	class MyList(list):
		__metaclass__ = listMetaclass
		# it call listMetaclass.__new__(MyList,'Mylist',(list,),MyList.__attrs__)

	L = MyList()
	print L.add(1)

	print 'an example of ORM (Object Relational Mapping) that requires dynamic modifying class defination using metaclass'
	# need ORM support, so marked
	if False:
		#define User class
		class User(Model): # Model func: __getattr__, __setattr__, __init__, save(), __metaclass__
			id = IntegerField('id') # Field
			name = StringField('username') #Field
			email = StringField('email') # Field
			password = StringField('password') # Field
		    # call __metaclass__; del id, name, email, password
		    # create __table__, __mappings__ (dict to save all)

		u = User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')

		u.save() # call save() from Model
		
		#now ORM
		class Field(object):
			def __init__(self,name,column_type):
				self.name=name
				self.column_type=column_type
			def __str__(self):
				return '<%s:%s>'%(self.__class__.__name__,self.name)

		class StringField(Field):
			def __init__(self,name):
				super(StringField,self).__init__(name,'varchar(100)') #call Field to init

		class IntegerField(Field):
			def __init__(self,name):
				super(IntegerField,self).__init__(name,'bigint')

		class ModelMetaclass(type):
			def __new__(cls,name,bases,attrs):
				if name=='Model':
					return type.__new__(cls,name,bases,attrs) # not change Model, only change User
				mappings = dict() # None dict
				for k,v in attrs.iteritems(): # original attrs: id, name, email, passwd
					if isinstance(v,Field): # all attrs are field instances
						print('Found mapping: %s==>%s'%(k,v)) 
						mappings[k] = v #save all attrs and values into dict mappings
				for k in mappings.iterkeys():
					attrs.pop(k) 
					#because we have mappings for save, delete old ones
				attrs['__table__'] = name #create new attrs for User: __table
				attrs['__mappings__'] = mappings # create __mappings__ for User
				return type.__new__(cls,name,bases,attrs) # creath a new definition for class User

		class Model(dict): # model is from dict
			__metaclass__ = ModelMetaclass

			def __init__(self, **kw):
				super(Model, self).__init__(**kw)

			def __getattr__(self, key): # self is a dict now: can get self[name] instead of self.name
				try:
					return self[key]
				except KeyError:
					raise AttributeError(r"'Model' object has no attribute '%s'" % key)

			def __setattr__(self, key, value): # can insert key-value into dict self
				self[key] = value

			def save(self):
				fields = []
				params = []
				args = []
				for k, v in self.__mappings__.iteritems(): # by metaclass, now attrs are saved in __mappings__
					fields.append(v.name)
					params.append('?')
					args.append(getattr(self, k, None))
				sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
				# use ',' to separate names in fields and params
				print('SQL: %s' % sql)
				print('ARGS: %s' % str(args)) #note args is a list

a=raw_input('Need see error & debug module?(y/n): ')
if a=='y':

	#https://docs.python.org/2/library/exceptions.html#exception-hierarchy
	print 'try...except...finally...'
	print 'first example:'
	try:
		print 'try...'
		r = 10/0
		print 'result:',r
	except ValueError,e:#ZeroDivison belongs to ValueError
		print 'ValueError:',e #e is the error string
	except ZeroDivisionError,e: #never be executed since ValueError
		print 'except:',e
	else:
		print 'no error!'
	finally: # finally will always be executed
		print 'finally...'
	print 'END\n'

	print '\ndefine DIY error class'
	class FooError(StandardError):
		pass
	def foo(s):
		n = int(s)
		if n==0:
			raise FooError('invalid value: %s'%s)
		return 10/n

	print 'common error types: ValueError, TypeError, IOError (contained in StandardError)'

	print '\n raise: raise an error for debuggers'
	try:
		print 'anything'
	except StandardError, e:
		print 'Error' #log
		raise # raise error info to debugger

	print 'Debug tactic 1:'
	print 'assert something, \'Error!\', something should be true, otherwise raise an AssertionError'
	#assert 1 != 1, 'error!'
	print 'use: python -O ***.py to ignore assert'

	import logging
	logging.basicConfig(level=logging.INFO)
	print '\nDebug tactic 2:'
	print 'use logging to record error files'
	print 'options: level= debug,info,warning,error'

	print '\nDebug tactic 3:'
	print 'single step running: pdb'
	print 'usage: python -m pdb ***.py'
	print 'enter l: check source code'
	print 'enter n: run one extra step'
	print 'enter p: check variable'
	print 'enter q: quit'

	print '\nDebug tactic 4:'
	print 'setup check point: pdb.set_trace()'
	import pdb
	#pdb.set_trace() 
	print 'program will pause at pdb.set_trace()'
	print 'enter c: continue to run'
	print 'enter p: check variable'

	print '\nDebug tactic 5:'
	print 'IDE: PyCharm'

	print '\nDebug tactic 6:'
	print 'Unit Test: write a unit test class'
	
	class Dict(dict):
		
		def __init__(self,**kw):
			super(Dict,self).__init__(**kw)

		def __getattr__(self,key):# so we can get self.a
			try:
				return self[key]
			except KeyError:
				raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

		def __setattr__(self,key,value): #so we can write self.a = b
			self[key] = value

	import unittest
	class TestDict(unittest.TestCase):

		def test_init(self):
			d = Dict(a=1,b='test')
			
			self.assertEquals(d.a,1)
			self.assertEquals(d.b,'test')#check values

			self.assertTrue(isinstance(d,dict))#check type

		def test_key(self):
			d = Dict()
			d['key'] = 'value' # check insertion
			self.assertEquals(d.key,'value')

		def test_attr(self): #check __setattr__()
			d = Dict()
			d.key = 'value'
			self.assertTrue('key' in d)
			self.assertEquals(d['key'],'value')

		def test_keyerrors(self):
			d = Dict()
			with self.assertRaises(KeyError):
				value = d['empty']
			# assert there will be keyerror if checking d['empty'] non-existing key
		def test_attrerror(self):
			d = Dict()
			with self.assertRaises(AttributeError):
				value = d.empty
		    # assert there will be attributeerror if checking d.empty non-existing attr

		def setUp(self):
			print 'setUp...'
		#setup and teardown are executed before and after any test function
		#can be used to setup preparation, such as open and close database 		
		def tearDown(self):
			print 'tearDown...'

	print 'add lines to the end of module for testing:'
	print r"if __name__ == '__main__':\
		unittest.main()"
	print 'or use python -m unittest ****.py'
	print '\ndoctest'
	print 'write down notes inside function such as it will be executed when doing python ***.py'
	print 'notation would be used as a test'
	print 'example:'
	print '''
	class Dict(dict):
    \''' # here is note start
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    \'''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

	if __name__=='__main__':
	    import doctest
	    doctest.testmod()'''

a=raw_input('Need see IO module?(y/n): ')
if a=='y':
	print 'read/write file'
	print 'functions: open, f.read(),f.close()'
	print 'open(): option: r - read, rb - read binary, w-write, wb - write binary'
	print 'read(size): read in size byte'
	print 'readline(): read one line'
	print 'readlines(): read all lines, return a list with each line for each index'
	print 'write(): write file; must add close or use with'

	print '\nwith: read + close + error_detection'
	print 'with open(\'/path/somefile.txt\',\'r\') as f:'
	print '    print f.read()'

	print '\nreadline: for loop'
	print 'for line in f.readlines():'
	print '    print(line.strip())'
	print 'line.strip(): delete \\n at the end of each line'

	print '\nwith: for write'
	print r"with open('/Users/path/some.txt','w') as f:"
	print r"    f.write('Hello,world!')"

	print '\nfile-like object: have open(), object have read(), e.g. StringIO: buffer in ram'

	print '\nautomatic code conversion: read file in non-ASCII format; example:'
	print 'import codecs'
	print r"with codecs.open('/path/some.txt','r','gbk') as f:"
	print '    f.read()'

	print '\n files and directories: os module'
	print 'import os'
	import os
	print 'os.name:',os.name
	print 'detailed os info:',os.uname()
	print 'env variables:',os.environ
	print 'obtain some env variables,e.g., path:',os.getenv('PATH')
	print 'current abs path:',os.path.abspath('.')
	print 'setup a new path:',os.path.join(os.path.abspath('.'),'mycompany1')
	print 'mkdir: mycompany1'
	os.mkdir(os.path.join(os.path.abspath('.'),'mycompany1'))
	print 'rmdir: mycompany1'
	os.rmdir(os.path.join(os.path.abspath('.'),'mycompany1'))
	print 'path split:',os.path.split(os.path.join(os.path.abspath('.'),'mycompany1'))
	print 'path split into path & extension:',os.path.splitext(os.path.join(os.path.abspath('.'),'pytutor.py'))
	print r"file rename: os.rename('some.txt','some.py')"
	print r"file remove: os.remove('some.py')"
	print r"file copy: using copyfile() from shutil module"
	print '\nprint all directories:'
	print [x for x in os.listdir('.') if os.path.isdir(x)]
	print '\nprint all .py files:'
	print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

	print '\npickling and up-pickling: change var of ram into savable format'
	print 'try import cPickle as Pickle'
	try:
		import cPickle as pickle
	except importError:
		import pickle
	d = dict(name='bob',age=20,score=88)
	print 'pickling d:',pickle.dumps(d)
	f = open('dump.txt','wb')
	pickle.dump(d,f)
	f.close()
	f = open('dump.txt','rb')
	d = pickle.load(f)
	print 'picking load d:',d
	f.close()
	os.remove('dump.txt')
	print '\npickling files can only be used in python of certain version'
	print 'better way is to save into standard format, such as JSON, XML'
	print r"https://docs.python.org/2/library/json.html#json.dumps"
	import json
	print 'json dump:',json.dumps(d)
	f = open('dump.txt','wb')
	json.dump(d,f)
	f.close()
	f = open('dump.txt','rb')
	d = json.load(f)
	print 'json load d:',d
	f.close()
	os.remove('dump.txt')

	print 'json dump for class object'
	print 'need to define a func to convert class into dict'
	print 'example 1:'
	class Student(object):
		def __init__(self,name):
			self.name = name
	s = Student('bob')
	def student2dict(std): #convert into dict
		return { # note: return a dict
			'name': std.name
		}
	print(json.dumps(s,default=student2dict))
	print 'example 2: use __dict__'
	print r"print(json.dumps(s, default=lambda obj: obj.__dict__))"
	print 'json load for class: convert json str into class instance'
	
	def dict2student(std):
		return Student(std['name'])

	print 'use: json.loads(json_str, object_hook=dict2student)'

a=raw_input('Need see Fork() module?(y/n): ')
if a=='y':
	import os
	import sys
	print 'fork(): cp current process to a child process, return both father and child process'
	print 'child: returns 0, use getppid() to get father id' 
	print 'father: returns children pid'
	print '\nExample: process (%s) start...'%os.getpid()
	pid = os.fork()
	if pid ==0:
		print 'I am child process (%s) and my parent is %s.'%(os.getpid(),os.getppid())
		sys.exit()
	else:
		print 'I (%s) just created a child process (%s).'%(os.getpid(),pid)
		sys.exit()

a=raw_input('Need see multiprocessing module?(y/n): ')
if a=='y':
	print '\nmultiprocessing module'
	from multiprocessing import Process
	import os
	import sys

	#child code
	def run_proc(name):
		print 'Run child process %s (%s)...'%(name, os.getpid())

	if __name__ == '__main__':
		print 'Parent process %s.'%os.getpid()
		p = Process(target = run_proc, args=('test',)) #create a child process with func and parameters
		print 'Process will start.'
		p.start()
		p.join() # synchronization
		print 'Process end.'

	print 'use pool to create batch of processes'
	from multiprocessing import Pool
	import time,random
	#import os

	def long_time_task(name):
		print 'Run task %s (%s)...' %(name,os.getpid())
		start = time.time()
		time.sleep(random.random()*3) # to make the func time consuming
		end = time.time()
		print 'Task %s runs %0.2f seconds.'%(name,(end-start))

	if __name__ =='__main__':
		print 'Parent process %s.'% os.getpid()
		p = Pool() # use Pool class to create instance
		#p=Pool(5), 5 is the max process number
		for i in range(5):
			p.apply_async(long_time_task,args=(i,)) # open a process with func and parameter in tuple
		print 'Waiting for all subprocesses done...'
		p.close() # cannot create new process
		p.join()
		print 'All processes done'

		print '\ncommunication between processes: Queue, Pipes'
		from multiprocessing import Process, Queue
		#import os,time,random
		def write(q):
			for value in ['A','B','C']:
				print 'Put %s to queue...' % value
				q.put(value)
				time.sleep(random.random())
		def read(q):
			while True:
				value = q.get(True)
				print 'Get %s from queue.'%value

		if __name__=='__main__':
			q = Queue() # create instance in parent proc
			pw = Process(target=write,args=(q,)) # create a process to wrtie with Queue()=q
			pr = Process(target=read,args=(q,)) # create a process to read with Queue()=q
			pw.start()
			pr.start()
			pw.join() # wait write proc to end
			pr.terminate() # read proc is dead loop. need force out

a=raw_input('Need see multithreading module?(y/n): ')
if a=='y':
	import time,threading
	def loop():
		print 'thread %s is running...'%threading.current_thread().name
		n = 0
		while n<5:
			n=n+1
			print 'thread %s >>> %s'%(threading.current_thread().name,n)
			time.sleep(1)
		print 'thread %s ended.' % threading.current_thread().name

	print 'thread %s is running.' % threading.current_thread().name
	t = threading.Thread(target=loop,name = 'LoopThread') # target = func, name = thread name
	t.start()
	t.join()
	print 'thread %s ended.' % threading.current_thread().name

	print '\nfor multithreading, since all threads share the same var, we need to lock and unlock var so it can only be changed by one thread a time'
	print 'funcs: lock = threading.Lock(),lock.acquire(),lock.release()'
	balance = 0;
	lock = threading.Lock()

	def change_it(n):
		global balance
		balance = balance + n
		balance = balance - n

	def run_thread(n):
		for i in range(100000):
			lock.acquire() # lock the var, only one thread can have the lock
			try:
				change_it(n)
			finally:
				lock.release() # work done, unlock
	t1 = threading.Thread(target=run_thread,args=(5,))
	t2 = threading.Thread(target=run_thread,args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print balance
	
	print '\nmultithreading on python can only use one CPU due to GIL'
	
	print '\nthreadlocal: p = threading.local(), p is global; \
	every thread can manage its own property of p'
	print 'useful in database visit for each thread'
	p = threading.local()
	def print_thread():
		print 'Student %s in thread (%s)'%(p.student,threading.current_thread().name)
	def process_thread(name):
		p.student = name
		print_thread()
	t1 = threading.Thread(target=process_thread,args=('Michael',),name='Thread 1')
	t2 = threading.Thread(target=process_thread,args=('Hao',),name='Thread 2')
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print 'distributed computing: managers ; (advanced)celery'
	if False:
		# taskmanager: register queue; write tasks into queue
		import random,time,Queue
		from multiprocessing.managers import BaseManager

		# send task queue
		task_queue = Queue.Queue()
		#receiver task queue
		result_queue = Queue.Queue()

		#inherit from basemanager
		class QueueManager(BaseManager):
			pass

		#online register two queue; use BaseManager.register()
		QueueManager.register('get_task_queue',callable=lambda: task_queue)
		QueueManager.register('get_result_queue',callable=lambda: result_queue)

		#use port 5000, setup key by creating a BaseManager instance
		manager = QueueManager(address=('',5000),authkey='abc')
		#start queue:
		manager.start()
		#get queue object
		task = manager.get_task_queue()
		result = manager.get_result_queue()
		#put several tasks
		for i in range(3):
			n = random.randint(0,10000)
			print 'Put task %d...'%n
			task.put(n)

		print 'Try get results...'
		for i in range(3):
			r = result.get(timeout=10)
			print 'Result: %s' %r
		#shut down 
		manager.shutdown()
		# task worker running on other computers
	if False:
		import time,sys,Queue
		from multiprocessing.managers import BaseManager

		#create QueueManager
		class QueueManager(BaseManager):
			pass

		#register
		QueueManager.register('get_task_queue')
		QueueManager.register('get_result_queue')
		#setup server
		server_addr = '127.0.0.1'
		print 'connect to server %s...'%server_addr

		#setup manager
		m = QueueManager(address=(server_addr,5000),authkey='abc')
		#connect to internet
		m.connect()
		#obtain Queue object:
		task = m.get_task_queue()
		result = m.get_result_queue()
		#get data from task, and send them by result
		for i in range(3):
			try:
				n = task.get(timeout=1)
				print 'run task %d * %d...' % (n,n)
				r = '%d * %d = %d' %(n,n,n*n)
				time.sleep(1)
				result.put(r)
			except Queue.Empty:
				print 'task queue is empty'

		print 'worker exit.'

a=raw_input('Need see regualr expression module?(y/n): ')
if a=='y':
	print r'''use RE (regular expression) for validating string: re module
	meaning: \ d : (no space) one number; e.g., 00\ d: for '007'
		\ w : one number or alphabet; e.g., \ w \ w \ d : for 'py3'
		.   : any char; e.g., 'py.' : for 'pyc'
		*   : any number of char, including 0 ; 
		+   : at least one char
		?   : zero or one char
		{n} : n chars ; e.g., \ d {3} : three numbers such as '010'
		{n,m}: n - m chars ; e.g., \ d {3,8} : such as '1234567'
		\ s : space or tab ; e.g., \ s + : at least one space
		     E.g., \ d {3} \ s + \ d {3,8} : '010   4567899'
		[ ] : range of selections; e.g., [ 0 - 9 a - z A - Z \ _ ] for one number or alphabet or _
			[ 0 - 9 a - z A - Z \ _ ] * for any number of chars selected from [ ]
		[ A | B] : A or B ; e.g., [ P | p ] ython : 'Python' or 'python'
		^    : start of line ; ^ \ d : use number to start a line
		$    : end of line ; \ d $ : use number to end a line
	'''
	import re

	test = r'^\d{3}\-\d{3,8}$'
	if re.match(test,'010-123456'):
		print 'ok'
	else:
		print 'failed'

	print '\ncan use re to split strings'
	print re.split(r'\s+','a b   c')
	print re.split(r'[\s\,]+', ' a  b,c ,,d , e')
	print re.split(r'[\s\,\;]+', 'a,b,; c d')

	print '\ngrou: use () to extract string'
	print  r'e.g., ^(\d{3})-(\d{3,8})$'
	m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
	print m.group(0),m.group(1),m.group(2)
	
	print 'split time; extract Hour, minute, second'
	t = '19:05:30'
	m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
	print m.groups()

	print '\nRE use greedy matching'
	print re.match(r'^(\d+)(0*)$','102300').groups()
	print 'add ? to avoid greedy'
	print re.match(r'^(\d+?)(0*)$','102300').groups()

	print '\npre-compile RE'
	re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
	print re_telephone.match('010-12345').groups()


a=raw_input('Need see internal modules module?(y/n): ')
if a=='y':
	print 'base64: encode a binary data with string txt using 64 elemental chars'
	print r'3 bytes -> 4 bytes; leftover 1 or 2 byte combined with \x00'
	print 'can display in web and email'
	import base64
	print base64.b64encode(r'binary\x00string')
	# base64.b64decode('erefge')
	print 'use urlsafe_b64encode for URL'
	print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
	print 'also get rid of ='
	print 'when decoding, add enough = , so the length in byte is multiple of 4'
	print 'base64 often used in URL, cookie, small binary data delivery of web'

	print '\nstruct: conversion between string and binary'
	import struct
	print struct.pack('>I',10240099) # >: big-endian (<: little endien); I: 4 bytes unsigned integer
	print struct.unpack('>IH','\xf0\xf0\xf0\xf0\x80\x80') #convert str to I: 4 bytes unsigned interger and H: two bytes unsigned integer
	#https://docs.python.org/2/library/struct.html#format-characters

	print '\nhashlib: compute MD5, SHA1'
	import hashlib
	md5 = hashlib.md5()
	md5.update('how to use md5 in python hashlib?')
	print md5.hexdigest()
	sha1 = hashlib.sha1()
	sha1.update('how to use sha1 in')
	sha1.update('python hashlib?')
	print sha1.hexdigest()
	print 'use: save passwords in the form of digest; safety'
	print 'salt: complexing simple password & distinguishing same passwds'
	print r"salted passwd = password+username+'the-salt'"

	print '\nXML: DOM and SAX'
	print 'DOM: read all XML into ram'
	print 'SAX: read XML node by node; need to resolve event'
	print 'usually use SAX, need start_element, end_element, char_data'
	
	from xml.parsers.expat import ParserCreate

	class DefaultSaxHandler(object):
	    def start_element(self, name, attrs):
	        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	    def end_element(self, name):
	        print('sax:end_element: %s' % name)

	    def char_data(self, text):
	        print('sax:char_data: %s' % text)

	xml = r'''<?xml version="1.0"?>
	<ol>
	    <li><a href="/python">Python</a></li>
	    <li><a href="/ruby">Ruby</a></li>
	</ol>
	'''
	handler = DefaultSaxHandler()
	parser = ParserCreate()
	parser.returns_unicode = True
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(xml)

	print '\nhtml: decode'
	from HTMLParser import HTMLParser
	from htmlentitydefs import name2codepoint

	class MyHTMLParser(HTMLParser):

	    def handle_starttag(self, tag, attrs):
	        print('<%s>' % tag)

	    def handle_endtag(self, tag):
	        print('</%s>' % tag)

	    def handle_startendtag(self, tag, attrs):
	        print('<%s/>' % tag)

	    def handle_data(self, data):
	        print('data')

	    def handle_comment(self, data):
	        print('<!-- -->')

	    def handle_entityref(self, name):
	        print('&%s;' % name)

	    def handle_charref(self, name):
	        print('&#%s;' % name)

	parser = MyHTMLParser()
	parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

a=raw_input('Need see PIL module?(y/n): ')
if a=='y':
	# sudo apt-get install python-imaging #ubuntu
	# sudo easy_install PIL
	import Image, ImageFilter
	if False:
		im = Image.open('/Users/michael/test.jpg')
		w , h =im.size
		#resize
		im.thumbnail(w//2,h//2)
		im.save('/Users/michael/thumbnail.jpg')
		#blur
		im2 = im.filter(ImageFilter.BLUR)

		print '\ngenerate alphabet validation image:'
		import Image,ImageDraw,ImageFont,ImageFilter
		import random
		#random char
		def rndChar():
			return chr(random.randint(65,90))
		#random color1
		def rndColor():
			return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
		#random color2
		def rndColor2():
			return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
		#240*60:
		width = 60*4
		height = 60
		image = Image.new('RGB',(width,height),(255,255,255))
		#create Font object:
		font = ImageFont.truetype('Arial.ttf',36) #maybe '/Library/Fonts/Arial.ttf'
		#create draw object:
		draw = ImageDraw.Draw(image)

		for x in range(width):
			for y in range(height):
				draw.point((x,y),fill=rndColor())
		for t in range(4):
			draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
		#blur
		image = image.filter(ImageFilter.BLUR)
		image.save('code.jpg','jpeg')

a=raw_input('Need see GUI module?(y/n): ')
if a=='y':
	print 'Tkinter'
	from Tkinter import *
	import tkMessageBox
	class Application(Frame):
		def __init__(self,master=None):
			Frame.__init__(self,master)
			self.pack()
			self.createWidgets()
		def createWidgets(self):
			self.helloLabel = Label(self,text='Hello,world!')
			self.helloLabel.pack()
			self.quitButton = Button(self,text='Quit',command=self.quit)
			#if button is clicked, command will be executed
			self.quitButton.pack()
			self.nameInput = Entry(self) 
			#input
			self.nameInput.pack()
			self.alertButton = Button(self,text='Hello',command = self.hello)
			self.alertButton.pack()
		def hello(self):
			name = self.nameInput.get() or 'world'
			tkMessageBox.showinfo('Message','Hello,%s'%name)			
		#Frame -> Widgets (button,label...) 
		# use pack() to add Widget into frame; grid() is advanced 
	app = Application()
	app.master.title('Hello World') #window title
	app.mainloop()

a=raw_input('Need see TCP/UDP module?(y/n): ')
if a=='y':
	print 'TCP connect: create a Sccket (create a link) on TCP'
	import socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#AF_INET: IPv4; AF_INET6: IPv6
	#SOCK_STREAM: TCP stream
	s.connect(('www.sina.com.cn',80))
	#input is a tuple!
	#standard WEB port 80
	s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
	#format: HTTP standard
	buffer = []
	while True:
		d = s.recv(1024) #1k byte
		if d:
			buffer.append(d)
		else:
			break
	data = ''.join(buffer)
	s.close()#close socket
	header, html = data.split('\r\n\r\n',1)
	print header
	with open('sina.html','wb') as f:
		f.write(html)	

	print '\nserver'
	import threading
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	

	#bind port and address of server
	s.bind(('127.0.0.1',9999))
	s.listen(5) # 5 is the max number of waiting link
	print 'Waiting for connection...'
	if False:
		while True:
			sock,addr = s.accept() #accept link from clients
			t = threading.Thread(target=tcplink,args=(sock,addr))
			#for any new link, create a new thread
			t.start()
	else:
		s.close() 

	def tcplink(sock, addr):
	    print 'Accept new connection from %s:%s...' % addr
	    sock.send('Welcome!')
	    while True:
	        data = sock.recv(1024)
	        time.sleep(1)
	        if data == 'exit' or not data:
	            break
	        sock.send('Hello, %s!' % data)
	    sock.close()
	    print 'Connection from %s:%s closed.' % addr
	
	if False: # client code
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 建立连接:
		s.connect(('127.0.0.1', 9999))
		# 接收欢迎消息:
		print s.recv(1024)
		for data in ['Michael', 'Tracy', 'Sarah']:
		    # 发送数据:
		    s.send(data)
		    print s.recv(1024)
		s.send('exit')
		s.close()

	print 'UDP: fast but unreliable'
	if False:
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.bind(('127.0.0.1',9999))
		print r"UDP server doesn't need listen"
		print 'Bind UDP on 9999...'
		while True: #server
			data, addr = s.recvfrom(1024)
			print 'Received from %s:%s.'%addr
			s.sendto('Hello, %s!'%data,addr)

		#client
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		for data in ['Michael', 'Tracy', 'Sarah']:
		    # 发送数据:
		    s.sendto(data, ('127.0.0.1', 9999))
		    # 接收数据:
		    print s.recv(1024)
		s.close()

a=raw_input('Need see send email module?(y/n): ')
if a=='y':
	print 'send by SMTP'
	from email.mime.text import MIMEText
	from email import encoders
	from email.header import Header
	from email.utils import parseaddr, formataddr
	from email.mime.multipart import MIMEMultipart
	from email.mime.base import MIMEBase
	import base64, getpass
	from_addr = raw_input('From: ')
	password = getpass.getpass()#raw_input('Password: ')
	smtp_server ='smtp.gmail.com'#raw_input('SMTP server:')
	to_addr = raw_input('To: ')

	def _format_addr(s):
		name,addr = parseaddr(s)
		return formataddr(( \
			Header(name,'utf-8').encode(),\
			addr.encode('utf-8') if isinstance(addr,unicode) else addr))

	#msg = MIMEText('hello,send by Python...','plain','utf-8') #pure txt
	msg = MIMEMultipart('alternative') # to attach file

	msg['From'] = _format_addr(u'hao li <%s>'%from_addr)
	msg['To'] = _format_addr(u'haoli <%s>'%to_addr)
	msg['Subject']=Header(u'来自SMTP的问候...','utf-8').encode()	
	#use the functions to encode chinese

	#email body # use alternative in MIMEMultipart: if HTML cannot be received, show in plain text
	msg.attach(MIMEText('send with file...','plain','utf-8'))

	#if want embed pic into text, use HTML
	msg.attach(MIMEText('<html><body><h1>Hello</h1>'+
		'<p><img src="cid:0"></p>'+
		'</body></html>','html','utf-8'))
	with open('/Users/haoli/Downloads/OneDrive/Pictures/Saved pictures/IMG_1042_JPG.jpg','rb') as f:
		#setup MIME and file name of attachment
		mime = MIMEBase('image','png',filename='test.png')
		#add necessary header information
		mime.add_header('Content-Disposition','attachment',filename='test.png')
		mime.add_header('Content-ID','<0>')
		mime.add_header('X-Attachement-Id','0')
		#read file
		mime.set_payload(f.read())
		#use Base64
		encoders.encode_base64(mime)
		#add to MIMEMultipart
		msg.attach(mime)	

	import smtplib
	server = smtplib.SMTP(smtp_server,587)# default SMTP port 25; gmail: 587
	server.starttls() # SSL safe connection
	server.set_debuglevel(1)
	server.login(from_addr,password)
	server.sendmail(from_addr,[to_addr],msg.as_string())
	server.quit()

	#send information in HTML
	msg = MIMEText('<html><body><h1>Hello</h1>'+
		'<p>send by <a href="http://www.python.org">Python</a>...</p>'+
		'</body></html>','html','utf-8') #send by Python with super-link to Python.org

	print '\nPOP3 receive email:'
	print '''step 1: download the encoded email
	step 2: decode email to readable email'''
a=raw_input('Need see receive email module?(y/n): ')
if a=='y':	
	import poplib, getpass
	import email
	from email.parser import Parser
	from email.header import decode_header
	from email.utils import parseaddr

	# 输入邮件地址, 口令和POP3服务器地址:
	email = raw_input('Email: ')
	password = getpass.getpass()#raw_input('Password: ')
	pop3_server = raw_input('POP3 server: ') #pop.gmail.com: 995

	# 连接到POP3服务器:
	server = poplib.POP3(pop3_server)
	# 可以打开或关闭调试信息:
	server.set_debuglevel(1)
	# 可选:打印POP3服务器的欢迎文字:
	print(server.getwelcome())
	# 身份认证:
	server.user(email)
	server.pass_(password)
	# stat()返回邮件数量和占用空间:
	print('Messages: %s. Size: %s' % server.stat())
	# list()返回所有邮件的编号:
	resp, mails, octets = server.list()
	# 可以查看返回的列表类似['1 82923', '2 2184', ...]
	#print(mails)
	# 获取最新一封邮件, 注意索引号从1开始:
	index = len(mails)
	resp, lines, octets = server.retr(index)
	# lines存储了邮件的原始文本的每一行,
	# 可以获得整个邮件的原始文本:
	msg_content = '\r\n'.join(lines)
	# 稍后解析出邮件:
	msg = Parser().parsestr(msg_content)
	# 可以根据邮件索引号直接从服务器删除邮件:
	# server.dele(index)
	# 关闭连接:
	server.quit()

	# decode email
	# indent用于缩进显示:
	def print_info(msg, indent=0):
	    if indent == 0:
	        # 邮件的From, To, Subject存在于根对象上:
	        for header in ['From', 'To', 'Subject']:
	            value = msg.get(header, '')
	            if value:
	                if header=='Subject':
	                    # 需要解码Subject字符串:
	                    value = decode_str(value)
	                else:
	                    # 需要解码Email地址:
	                    hdr, addr = parseaddr(value)
	                    name = decode_str(hdr)
	                    value = u'%s <%s>' % (name, addr)
	            print('%s%s: %s' % ('  ' * indent, header, value))
	    if (msg.is_multipart()):
	        # 如果邮件对象是一个MIMEMultipart,
	        # get_payload()返回list，包含所有的子对象:
	        parts = msg.get_payload()
	        for n, part in enumerate(parts):
	            print('%spart %s' % ('  ' * indent, n))
	            print('%s--------------------' % ('  ' * indent))
	            # 递归打印每一个子对象:
	            print_info(part, indent + 1)
	    else:
	        # 邮件对象不是一个MIMEMultipart,
	        # 就根据content_type判断:
	        content_type = msg.get_content_type()
	        if content_type=='text/plain' or content_type=='text/html':
	            # 纯文本或HTML内容:
	            content = msg.get_payload(decode=True)
	            # 要检测文本编码:
	            charset = guess_charset(msg)
	            if charset:
	                content = content.decode(charset)
	            print('%sText: %s' % ('  ' * indent, content + '...'))
	        else:
	            # 不是文本,作为附件处理:
	            print('%sAttachment: %s' % ('  ' * indent, content_type))
	def decode_str(s):
	    value, charset = decode_header(s)[0]
	    if charset:
	        value = value.decode(charset)
	    return value

	def guess_charset(msg):
	    # 先从msg对象获取编码:
	    charset = msg.get_charset()
	    if charset is None:
	        # 如果获取不到，再从Content-Type字段获取:
	        content_type = msg.get('Content-Type', '').lower()
	        pos = content_type.find('charset=')
	        if pos >= 0:
	            charset = content_type[pos + 8:].strip()
	    return charset










































































			









































