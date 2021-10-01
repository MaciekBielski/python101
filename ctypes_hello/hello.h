#ifndef __HELLO_H__
#define __HELLO_H__

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point start;
    Point end;
    const char *label;
} Line;

typedef enum { LINE_START, LINE_END } LineSide;

int line_zalloc(Line **l, const char *label);
void line_free(Line **l);
void line_show(Line *l);
void line_set_point(Line *l, Point *p, LineSide ls);
double line_len(Line *l);

#endif /* __HELLO_H__ */
