#!/bin/sh

cd AsyncCLI
python setup.py install
cd ..

cp kodiremote.py /usr/local/bin/kodiremote
cp kodix.py /usr/local/bin/kodix

chmod a+rx /usr/local/bin/kodiremote
chmod a+rx /usr/local/bin/kodix
