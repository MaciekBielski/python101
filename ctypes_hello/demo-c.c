#include <stdio.h>

#include "hello.h"

int main()
{
    Line *l;
    line_zalloc(&l, "HELLO_Line");
    line_show(l);

    Point points[] = {{5, 5}, {8,9}};
    line_set_point(l, &points[0], LINE_START);
    line_set_point(l, &points[1], LINE_END);
    line_show(l);

    printf("%s: length = %lf\n", l->label, line_len(l));

    line_free(&l);
    if (l)
        puts("[!] Line should be NULL");

    return 0;
}
