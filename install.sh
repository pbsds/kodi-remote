#!/bin/sh

echo "Make sure you run this as root!"
echo "sudo sh install.sh"

cd AsyncCLI/
python setup.py install
cd ..

echo "Installing kodiremote..."
cp kodiremote.py /usr/local/bin/kodiremote
chmod a+rx /usr/local/bin/kodiremote

echo "Installing kodix..."
cp kodix.py /usr/local/bin/kodix
chmod a+rx /usr/local/bin/kodix
