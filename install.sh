#!/bin/sh

chmod a+x kodiremote.py
chmod a+x kodix.py

cd AsyncCLI
python setup.py install
cd ..

ln -s kodiremote.py /usr/local/bin/kodiremote
ln -s kodix.py /usr/local/bin/kodix
