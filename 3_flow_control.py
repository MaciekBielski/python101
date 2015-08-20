#!/usr/bin/python3

print( '1.\t''for iterates over lists or strings')
a='simple string'
b=[11,22,33]

print( '\t',)
for i in a:
  print(i,end='')
else:
  print('')

print( '\t',)
for i in b:
  print(i,end='')
else:
  print('')

# iterating over a copy of a sequence for making modifications
# without a copy it would be an infinite loop

print('2.\t', end='')
for bb in b[:]:
  print( bb, end='')
  if bb>=22:
    b.insert(0,bb)
else:
  print( '')
print('\t',b)

print('3.\tprime numbers:',end='')
for n in range (2,10):
  for m in range (2,n):
    if n%m==0:
      break
  else:
    print(n,end='')
else:
  print('')

# predefined clean-up actions will be runned automatically
# binary file reading does not look on newline sign
print('4.')
with open('file1.txt','r') as f:
  for l in f:
    print('\t',l,end='')
  else:
    print('')

# watch the difference between reading line and reading characters !!!
print('5.')
with open('file1.txt','r') as f:
  for l in f.readline():
    print(' ',l,end='')
  for l in f.readline():
    print(' ',l,end='')
  else:
    print('')
