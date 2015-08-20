#!/usr/bin/python3
import functools

# LISTS - is not a sequence
a = [2, 4, 8, 16, 32]
e = 64
L = [128, 256]

a.append(e)
a.extend(L)
a.remove(8)     # it's not position but a value! -> indexes change
del a[3]        # remove vs. delete: deleting 32
a.insert(2,9)
print('1.\t',a)
a.pop(3)
a.insert(3,9)
a.reverse()    # reversed(seq) only for sequences
print('2.\t',a, '\t9 occurs',a.count(9), 'times')

# FUNCTIONAL PROGRAMMING

# filtering
f13 = lambda x: x%13==3
print('3.\t''filter:',filter(f13,range(0,100)))

# map
flen = lambda x: len(x)
in_tuple = ('a','bb','ccc','dddd','eeeee')
print('4.\t''tuple:',in_tuple,'lengths by map:',map(flen,in_tuple))

# reduce - call a function on first two elements, then on result and third element and so on...
# building alphabet by list comprehensions
fadd= lambda a,b: b+'_'+a
alph= lambda :range(ord('a'),ord('z')+1)
in_str= [ chr(i) for i in alph() ]
print('5.\t''reduce: ',functools.reduce(fadd,in_str))

# more fancy list comprehension
# two fors make a carthesian multiplication
lc=[ (a,b) for a in alph() for b in alph() if a==b]
# generator comprehesion instead of list comprehension
lc=( (chr(a[0]),chr(a[1])) for a in lc )
tts=lambda t: t[0]+'_'+t[1].upper()
print('6.\t',list(map(tts,lc)))

# nested list comprehension - matrix transposition
# [ [ [third] second] first ] etc...
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat_transp=[ [ el[i] for el in mat ] for i in range(4) ]
print('7.\t',mat_transp)

# convert a list tu a tuple
print('8.\t',list(zip(*mat)))

# TUPLE - immutable
et = ()         # empty tuple
st = 'only',    # a tuple with single element - comma!
a,b = ('first','second')
c=('aaa','bbb','ccc')
print('9.\t',et,'len: ',len(et),'\t',st,'len: ',len(st),'\tunpacked:',a,b)

# SETS - unordered, no duplicates
# operations on sets: a-b, a|b, a&b, a^b
fruits=['pear', 'plum', 'currant', 'blueberry', 'raspberry', 'strawberry', 'blackberry', 'gean' ]
fruits_set = set(fruits)
print('10.\t', fruits_set)

# set comprehensions and containment
sc={ x for x in 'abracadabra' if x not in 'abc' }
print('11.\t',sc)

# DICTIONARIES - keys have to be immutable: strings, numbers, tuples(of immutable types)
# lists cannot be used as a key - they are mutable
# dictionaries are mutable
d1=dict([('malina','raspberry'),('jezyna','blackberry'),('borowka','blueberry'),('czeresnia','gean')])
d2=dict(gruszka='pear', porzeczka='currant', sliwka='mutable_test')
d2['sliwka']='plum'
print('12.\t', sorted(d1.keys()))
print('13.\t', [ d1[k] for k in sorted(d1.keys()) ])
print('14.\t', [ (k,d2[k]) for k in sorted(d2.keys()) ])

# LOOPING
# 1) enumeration - indices as keys
print('15.\t',end='')
for i,f in enumerate(fruits):
  print(i,f,'| ',end='')
else:
  print('')

# 2) convienient way of building correspondence between two lists by transposition
d1_keys = d1.keys()
d1_vals = [ d1[k] for k in d1_keys ]
print('16.\t',end='')
for k,v in zip(d1_keys,d1_vals):
  print(k,v,'|',end='')
else:
  print('')

# 3) looping through dictionary in a convienient way
print('17.\t',end='')
for k,v in d2.items():
  print(k,v,'|',end='')
print('')
