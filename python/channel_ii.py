#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 Michel Barbeau.

import numpy
from gnuradio import gr

class channel_ii(gr.sync_block):
    "Classical or quantum channel abstraction"
    def __init__(self):
        gr.sync_block.__init__(self,
            name="channel_ii",
            in_sig=[numpy.uint32],
            out_sig=[numpy.uint32])

    def work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        return len(output_items[0])

