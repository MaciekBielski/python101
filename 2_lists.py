#!/usr/bin/python3

s ='Lists are mutable\n' 
print(s)
a = ['first','second',3]
print( 'indexing returns an item, slicing returns a shallow copy')
print( 'a[1]:',a[1])
print( 'a[:]:',a[:], '\telements',len(a))
b = [1,3]
c = [4,6]
print( 'concatenation ',b+c)
b[0]=c[0]=9
b.append(8); c.append(8)
print( 'changes ',b+c)
b[1:2]=c[2:3]=[]
print( 'removing by slices: ',b+c)
# if a slice is rvalue it returns a shallow copy
# if a slice is lvalue it corresponds to elements

a, b = 0, 1
while b<25:
  a,b=b,a+b
  print(a,' ',end='')
print('')

