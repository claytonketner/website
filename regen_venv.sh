#!/bin/bash

# Move the current .virtualenv so that it can be restored if this fails
if [ -d .virtualenv ]; then
    mv .virtualenv .virtualenv_old
fi
virtualenv .virtualenv
echo "Virtualenv created as .virtualenv"

# Copy in files from .venv_packages
# We could do a DFS or something, but that's hard
if [ -d .venv_packages ]; then
    cp -R .venv_packages/lib/python2.7/site-packages/* .virtualenv/lib/python2.7/site-packages/
else
    echo "Failed - no .venv_packages directory"
    echo "Restoring previous .virtualenv"
    mv .virtualenv_old .virtualenv
    exit 1
fi

source .virtualenv/bin/activate
pip install -r requirements.txt

echo "Success. Old virtualenv is at .virtualenv_old"
