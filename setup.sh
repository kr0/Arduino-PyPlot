#!/bin/bash
echo "Setting up"
virtualenv env
env/bin/pip install matplotlib
env/bin/pip install drawnow
env/bin/pip install pyserial
