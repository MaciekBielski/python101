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

    def __init__(self, **kwargs):
        self._j= 500 + (kwargs['k'] if 'k' in kwargs else 0)

    def f(self):
        print('\tA class-scope attribute: ', self.i, 'instance attribute:',self._j)

print('1.',end='')
t = ExClass()
u = ExClass()

# Over-shadowing class-attribute with instance-attribute
t.f()
t.i = 666
t.f()

# Class-attributes affected only (instance attributes preferred!)
ExClass.i = 404
t.f()
u.f()
print('')


class Derved(ExClass):

    class Inner:
        def reach_outer(self, outer):
            print("\tfrom outer: {}", outer.i)
            outer.i = 987
            print("\tfrom outer: {}", outer.i)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._j=222

    def g(self):
        inner = self.Inner()
        inner.reach_outer(self)

s = Derved()
print('2.',end='')
s.g()
s.f()
print('')


def indented(f):
    def wrapper(dummy):
        return f'\t{f(dummy)}'
    return wrapper


class Dummy:
    def __init__(self, **kwargs):
        self._label = kwargs['label'] if 'label' in kwargs else 'dummy'

    #geterr-setter
    def label(self, l = None):
        if l: self._label = l
        return self._label

    #decoration by non-member function
    @indented
    def __str__(self):
        return f'label: {self.label()}'


print('3.',end='')
# v = Dummy()
print(Dummy(label='idiomatic'))
print(Dummy())

