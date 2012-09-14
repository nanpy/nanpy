cd firmware
export BOARD=uno
make -f ../Makefile clean
make -f ../Makefile
make -f ../Makefile upload
