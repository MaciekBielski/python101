Description
-----------
An example of calling C code (provided by a library) from Python using ctypes.
Especially shows how to pass a pointer as an out-argument, so that resources are
allocated on the library side and the pointer is set respectively.

Also provides a simple C-client implementation, just to verify the library
itself.

Requires an external ctypesgen tool [4] (or a link) to be at ./ctypesgen path.


Launching
---------
$ make clean && make
$ demo-c                // (optional, runs the C-client)
$ ./gen-bindings.sh
$ demo.py


References
----------
[1]: https://dbader.org/blog/python-ctypes-tutorial
[2]: https://dbader.org/blog/python-ctypes-tutorial-part-2
[3]: https://docs.python.org/3/library/ctypes.html
[4]: https://github.com/ctypesgen/ctypesgen
