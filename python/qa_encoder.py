#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 Michel Barbeau.
# Version: August 23, 2015 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from encoder import encoder
from channel_ii import channel_ii
from decoder import decoder

class qa_encoder (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
	print '--- encoder - test_001_t\n'
	# create a data sink
	src=blocks.vector_source_i([0, 1, 0, 1, 0])
	# create encoder
        enc = encoder()
	# create quantum channel
        q_ch = channel_ii()
	# create classical channel
        c_ch = channel_ii()
	# create decoder
        dec = decoder()
	# interconnections
        self.tb.connect((src,0), (enc,0))
        self.tb.connect((enc,0), q_ch)
        self.tb.connect((enc,1), c_ch)
        self.tb.connect(q_ch, (dec,0))
        self.tb.connect(c_ch, (dec,1))
	self.tb.msg_connect(dec,"feedback",enc,"feedback")
	self.tb.msg_connect(enc,"ciphertext",dec,"ciphertext")
        self.tb.run()

if __name__ == '__main__':
    gr_unittest.run(qa_encoder, "qa_encoder.xml")
