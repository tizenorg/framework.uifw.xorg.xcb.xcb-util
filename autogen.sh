#! /bin/sh
libtoolize --force
autoreconf -v --install || exit 1
./configure "$@"
