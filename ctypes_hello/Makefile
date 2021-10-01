CC		= gcc
CFLAGS += -fPIC -std=c11
SRCS	= $(wildcard $(PWD)/*.c)
OBJS	= $(patsubst $(PWD)/%.c,$(PWD)/%.o,$(SRCS))


all: libhello.so demo-c

clean:
	rm -rf ./*.o ./*.so ./demo-c

libhello.so: hello.o
	$(CC) -shared $^ -lm -o $@

demo-c: demo-c.o
	$(CC) -o $@ -L. -lhello -Wl,-rpath,$(PWD) $^
