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

	





