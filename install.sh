#!/bin/sh

chmod a+x kodiremote.py
chmod a+x kodix.py

cd AsyncCLI
python setup.py install
cd ..

cp kodiremote.py /usr/local/bin/kodiremote
cp kodix.py /usr/local/bin/kodix
