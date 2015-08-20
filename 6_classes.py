#!/usr/bin/python

class ExClass:
  i=313
  def __init__(self,k=0):
    print(self.__class__,'init')
    self.j=500+k
  def f(self):
    print('A predefined attribute: ',self.i, 'tuned attribute:',self.j)

print('1.\t',end='')
t = ExClass(166)
print('2.\t',end='')
t.f()

# a derived class does not inherit attributes of a base class (?)
class Derved(ExClass):
  def __init__(self):
    print(self.__class__,'init')
    self.base=ExClass(33)

  def g(self):
    print('id:',id(self))
    self.base.f()

print('3.\t',end='')
s = Derved()
print('4.\t',end='')
print('all attributes of an object:\n',dir(s))
print('5.\t',end='')
s.g()
