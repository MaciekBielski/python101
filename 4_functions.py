#!/usr/bin/python3

x = 0
y = 1
def sillyfun(*args):
    # Needed to modify global variable
    global x
    print('y read-only from global-scope: ',y)
    x = 6

sillyfun()
print('global x: ', x)
print('global y: ', y)
print('')


def ask(prompt, retries=3, complaint='try again'):
    '''varargs function, if no ifs is reached then .__doc__ is printed'''
    while True:
        ri=raw_input(prompt)
        if ri in ('a','b','c'):
            print('abc')
            return
        retries -= 1
        if retries == 0:
            raise IOError('bad letters')
        print(complaint)
print(ask.__doc__)

# ask('#fool>',2,'horror!!!')
print('''''')

def fib(n):
    '''remembering default value between subsequent calls,
        the value of default argument is evaluated only once and remembered if returned to the upper scope '''
    def fib_in(l=[]):
        if len(l)==0:
            l += [0,1]
        else:
            l.append(l[-1]+l[-2])
        return l
    for i in range(1,n-1):
        fib_in()
    else:
        print(fib_in())
fib(8)

def forgt(n,L=[]):
    '''to forget the default argument value between subsequen calls use None'''
    if L==None:
        L=[]
    for nn in n:
        L.append(nn)
    return L
print(forgt([10,20]))
print(forgt([30,40]))
print(forgt([50,60]))
print('\n','-'*40)

def default_args_test(word,c='O',i=8):
    ''' function with keyword arguments, can be called with args id different order
        kwargs always at the end, keyword argument has to follow positional argument '''
    print('word: ',word,' character: ',c, ' integer: ',i)

default_args_test('first')
default_args_test('second','B')
default_args_test('third','C',69)
default_args_test('fourth',i=11,c='D')
default_args_test('fifth',i=101)
print('\n','-'*40)

def tuple_args(*args):
    ''' a function can be called with a variable number of args '''
    for a in args:
        print(a,end='-')
    else:
        print('\n','-'*40)
tuple_args('nokia','samsung','htc')
# definition of a tuple (), [] or {}
tuple2=('audi','volvo','kia')
# Use asterisk to expand the tuple
tuple_args(*tuple2)

def dict_args(**kwargs):
    ''' a function can be prepared to be called with a dictionary: set of pairs variable=value'''
    for kw in sorted(kwargs.keys()):
        print(kw,':',kwargs[kw],'\t',)
    else:
        print('\n','-'*40)
dict_args(aaa=111,bbb=222,ccc=333,word='eeeeend!')

#definition of a dictionary outside a function prototype
dict2={'elem1':'alfa', 'elem2':'beta', 'zero':'finish'}
dict_args(**dict2)

# lambda expressions
pair_key = lambda pair: pair[1]
pairs_tab = [('a',4), ('bb',3), ('ccc',2), ('zzzzzzz',0)]
pairs_tab.sort(key = pair_key)
print(pairs_tab)
