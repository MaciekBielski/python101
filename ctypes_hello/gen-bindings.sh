#!/bin/bash

set -euxo pipefail

FLAGS="-I${PWD} -L${PWD} -lhello"
HEADERS="${PWD}/hello.h"

rm -rf hello.py
./ctypesgen/run.py ${FLAGS} ${HEADERS} -o hello.py

# ./demo.py
