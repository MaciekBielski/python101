#!/usr/bin/python3

if __name__ == '__main__':
    print('Executed directly, not as a module\n\n')

s ="Strings are immutable, len: "
print(s,len(s))
x = str(83)
print('1.\t','int to string',x[0],x[1])
print('2.\t''str to int',int(x))
print('3.\t''int to ascii', chr(83))
print('4.\t''ascii to int', ord(chr(83)))
print('5.\t',r'this is a raw string \n\t')
print('7.\t','concatenation - only for literals\n\t','tra'+3*'la')
a = 'concatenation '
b = 'for variables'
print('7.\t',a + b)
c = 'PYTHON'
print('8.\t',c + '- first letter: ' + c[0] + ', last letter: ' + c[-1])
print('9.\t','ranges [start, stop), so for three letters [0:3] ->' + c[0:3])
print('10.\t','whole word without the last letter, [0:-1] -> ' + c[0:-1])

# # converting values to strings:
# # str() - generate human-readable representation
# # repr() - generate interpretation readable by the interpreter

print('11.\t')
for i in range(1,6):
  print('\t',repr(i).rjust(2), repr(i**2).rjust(3), repr(i**3).rjust(4))

print('12.\n\tWith zero filling')
for i in range(1,6):
  print('\t{0:02d} {1:3d} {2:3d}'.format(i,i**2,i**3))

print('13.\t')
from math import pi
print(f'{" ":10}f-string: PI = {pi:.4f}')

print('14.\t')
values_dict=dict(first='alpha', second='beta', third='gamma')
print('\t1:{first:9s}2:{second:9s}3:{third:9s}'.format(**values_dict))

