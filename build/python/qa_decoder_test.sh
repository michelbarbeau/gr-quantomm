#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/barbeau/gr-quantomm/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/barbeau/gr-quantomm/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/barbeau/gr-quantomm/build/swig:$PYTHONPATH
/usr/bin/python2 /home/barbeau/gr-quantomm/python/qa_decoder.py 
