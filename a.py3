#!/usr/bin/python3 -i

import binascii

ltrs = []

with open('/tmp/a.txt', 'rb') as f:
    for l in f:
        ltrs.append(chr(int(l[:-1], 2)))

resp = 'Bla bla bla'

# out = [ print('{}: {}'.format(str(bin(ord(l)))[2:].zfill(8), l)) for l in resp ]
out = [ '{}'.format(str(bin(ord(l)))[2:].zfill(8), l) for l in resp ]

i = 0
for v in out:
    i += 1
    e = '\n' if i%8 == 0 else ' '
    print(v, end=e)
else:
    print('')


