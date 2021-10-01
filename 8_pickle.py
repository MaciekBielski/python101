#!/usr/bin/python
import sys
import pickle
import string
import datetime
import re
import struct

puzzle="Look at the next 8 lines\ncdatetime\ndatetime\np0\n(S'\x07\xde\x0c\x0c\x08\x1e\x14\x05\x8d\x9f'\np1\ntp2\nRp3\n.\nThat was a pickle version of the current datetime\nCan you tell me the number of microseconds you can find in the object (after you de-pickle it)?s\n"
test=r'\x07\xde\x0c\x0c\x08\x1e\x14\x05\x8d\x9f'
datestring='2012-12-12 10:11:14.453867'

def depickle(pickled):
  obj = string.split(pickled,'\n')
  s=pickle.loads(part)
  print s

# create datatime object and dump it to string
obj = datetime.datetime.now()
print repr(pickle.dumps(obj))
#e=struct.unpack('63s',test)
#dtp = struct.pack('26s',test)
