#!/usr/bin/python
import functools

# object has to implement a function iter() that returns iterator object, iterator object has to have
# function next() which access elements in the iterator one at a time and raises StopIteration exception
# when there is no more elements

# generator - uses yield to return data, yield remembers last position called
# __iter()__ and next() are created automatically
def rev(data):
  for e in range(0,len(data),2):
    yield data[e:e+2]

print('1.\t',end='')
for c in rev('simple string'):
  print(c,'_',sep='',end='')
else:
  print('')

# functions for iterable objects
print('2. [with list comprehension]')
if any([x<0 for x in range(5,-2,-1)]): 
  print('\tthere is a negative object')

# generator expressions - when you do not want to precompute the whole list
# at the beginning
print('3. [with generator comprehension]')
if all((x>3 for x in range(4,8,1))):
  print('\tall objects are positive')

# decorators - uses function closure, inner function remembers enclosing
# namespace from the definition time, the inner function is redefined each
# time the outer function is called

# outer function serves as a constructor for object of inner function
# *args - extract them at calling time and treat as positional parameters
# **kwargs - the same but treat as named parameters
# DECORATORS ARE GREAT FOR LOGGING PURPOSES!!!

print('4. [function decorator]')
def dashWrapped(f):
  def wrapper(*params, **kwparams):
    print('-'*40)
    f(*params, **kwparams)
    print('-'*40)
  return wrapper

@dashWrapped
def simpleFun(*params):
  oper = lambda a,b: a+'_'+b
  print(functools.reduce(oper,*params))

simpleFun( [ chr(x) for x in range(ord('a'),ord('h')+1) ] )

# since parenthesis trigger function invocation then if we want decorator
# with parameters we have to add another intermediate level
print('5. [function decorator with arguments]')

def wrapperProducer(sgn,wd):
  def tunableWrapper(fun):
    def wrapped(*args,**kwargs):
      print(str(sgn)*wd)
      fun(*args,**kwargs)
      print(str(sgn)*wd)
    return wrapped
  print('+++decorator construction+++')
  return tunableWrapper

@wrapperProducer('%',47)
def simpleFun2(*params):
  oper = lambda a,b: a+'_'+b
  print(functools.reduce(oper,*params))

print('+++before execution+++')
simpleFun2( [ chr(x) for x in range(ord('A'),ord('H')+1) ] )

# the same realized with class
# without arguments it's straightforward
print('6. [class-oriented decorator without arguments]')

class AsteriskWrapped(object):
  def __init__(self,f):
    print('\tinitialization')
    self.f = f

  def __call__(self,*args,**kwargs):
    print('*'*40)
    self.f(*args,**kwargs)
    print('*'*40)

@AsteriskWrapped
def simpleFunAgain(*params):
  oper = lambda a,b: a+'_'+b
  print(functools.reduce(oper,*params))

simpleFunAgain( [ chr(x) for x in range(ord('i'),ord('p')+1) ] )

# and now with arguments - different parameters are passed at different time
# comparing to the previous case: __call__ is only called once as a part of
# decoration process!! __call__ is invoked by parenthesis ()
print('7. [class-oriented decorator with arguments]')

class TunableWrapped(object):
  def __init__(self,sign,width):
    print('__init__ part')
    self.sign = sign
    self.width = width

  def __call__(self,f):
    print('__call__ part')
    def wrapper(*args, **kwargs):
      print(str(self.sign)*self.width)
      f(*args, **kwargs)
      print(str(self.sign)*self.width)
    return wrapper

@TunableWrapped('^',33)
def simpleFunRevisited(*params):
  oper = lambda a,b: a+'_'+b
  print(functools.reduce(oper,*params))

print('+++before execution+++')
simpleFunRevisited( [ chr(x) for x in range(ord('I'),ord('P')+1) ] )
