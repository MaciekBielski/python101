#!/usr/bin/python3
'''
- A child class inherits: parent class parameters and methods
- Inherited methods are invoked with current instance parameters
- Instance first looks for its own parameters, then class chierarchy
  parameters, also created after instance initialization.
- Parameters added only to instance are not accessible to anything else
'''

class ExClass:
    i=313

    def __init__(self,k=0):
        print(self.__class__)
        self.j=500+k

    def f(self):
        print('A predefined attribute: ',self.i, 'tuned attribute:',self.j)

print('1.\t',end='')
t = ExClass(166)
print('2.\t',end='')
t.f()

class Derved(ExClass):
    i=88

    def __init__(self):
        print(self.__class__)
        self.j=222

    def g(self):
        print('id:',id(self))

print('3.\t',end='')
s = Derved()
print('4.\t',end='')
s.g()
print('5.\t s.i={}'.format(s.i))
u = Derved()
