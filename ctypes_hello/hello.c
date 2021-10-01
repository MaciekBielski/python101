#define _POSIX_C_SOURCE 200809L

#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "hello.h"

int line_zalloc(Line **l, const char *label)
{
    Line *out = malloc(sizeof(Line));
    if (!out)
        return -1;

    out->start.x = out->start.y = 255;
    out->end.x = out->end.y = 255;
    out->label = strndup(label, 128);
    *l = out;
    printf("Allocated: %s\n", out->label);

    return 0;
}

void line_free(Line **l)
{
    if (*l == NULL)
        return;

    free((void*)(*l)->label);
    (*l)->label = NULL;
    free(*l);
    *l = NULL;

    puts("Line cleaned up");
}

void line_show(Line *l)
{
    printf("%s: (%d, %d) -> (%d, %d)\n",
           l->label, l->start.x, l->start.y, l->end.x, l->end.y);
}

void line_set_point(Line *l, Point *p, LineSide ls)
{
    Point *pt = NULL;

    switch(ls) {
        case LINE_START:
            pt = &l->start;
            break;
        case LINE_END:
            pt = &l->end;
            break;
        default:
            puts("[!] Wrong line end specified");
            return;
    }
    *pt = *p;
}

double line_len(Line *l)
{
    return sqrt(pow(l->end.x - l->start.x, 2) +
                pow(l->end.y - l->start.y, 2));
}
