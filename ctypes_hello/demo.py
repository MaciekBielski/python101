#!/usr/bin/env -S python3

from hello import *

my_label = c_char_p(b"SIMPLE_line")

line_p = pointer(Line())
# NOTE: No segfault, line_p zero-initialized in Python
line_show(line_p)

ret = line_zalloc(byref(line_p), my_label)
line_show(line_p)

points = [Point(5,5), Point(8,9)]
line_set_point(line_p, points[0], LINE_START)
line_set_point(line_p, points[1], LINE_END)
print(f'{line_p.contents.label}: length = {line_len(line_p)}')

line_free(byref(line_p))
# Uncomment for segfault
# line_show(line_p)
