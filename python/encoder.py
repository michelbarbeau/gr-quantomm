#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Michel Barbeau.
# Version: January 6, 2016 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

import numpy
from gnuradio import gr
import random
import pmt # polymorphic data types
import sys

class encoder(gr.interp_block):
    "Quantum encoder"
    # debug mode flag
    debug_stderr=True
    # rectilinear basis & diagonal basis angles
    basis = [[0, 90], [45, 135]]
    # plain text buffer
    plain_text = []
    # from-decoder feedback 
    feedback = []
    # potential key bit buffer
    key_bit = [0] # first item is random and not used (feedback always neg)
    # selected random bases
    sel_basis = 0 # first item is random and not used

    # constructor
    def __init__(self):
        gr.interp_block.__init__(
            self,
            name="encoder",
	    # input signature
	    # in port for plain text 
            in_sig = [numpy.uint32],	
            # output signature
	    # out port of photon angles: 0s, 90s, 45s and 135s 
            out_sig = [numpy.uint32,
	    # out port of selected bases: 0s and 1s
                       numpy.uint32],
	    interp = 2) # interpolation ratio
	# asynchronous from-decoder feedback port, 0s (neg.) and 1s (pos.) 
 	self.message_port_register_in(pmt.intern('feedback'))
        self.set_msg_handler(pmt.intern('feedback'), self.handle_msg)
	# asynchronous encrypted data port, 0s and 1s
 	self.message_port_register_out(pmt.intern('ciphertext'))

    # from-decoder feedback port handler
    def handle_msg(self, msg):
	# save the feedback from-decoder 
	self.feedback.extend(pmt.to_python(msg))
	# encrypted data
	ciphertext = []
        # consumed feedback
        feedback = []
        # consumed plain text
        plaintext = []
        # consume feedback from encoder
	for _ in range(min(len(self.feedback),len(self.plain_text))):
		# consume a feedback item
		f = self.feedback.pop(0)
                feedback.append(f)
		# consume a key bit
		k = self.key_bit.pop(0)
		if f: # positive feedback?
			# get a data bit
			d = self.plain_text.pop(0)
			plaintext.append(d)
			# post encrypted data bit
			ciphertext.append(k^d)
	if self.debug_stderr: 
           sys.stderr.write("encoder.handle_msg():feedback: " + \
                str(feedback) + "\n")
	if self.debug_stderr: 
           sys.stderr.write("encoder.handle_msg():plain text: " + \
                str(plaintext) + \
		" cipher text: " + str(ciphertext) + "\n")
        # post encrypted data
        self.message_port_pub(pmt.intern('ciphertext'),
           pmt.to_pmt(ciphertext))

    # main
    def work(self, input_items, output_items):
	# buffer input data
	self.plain_text.extend(input_items[0])
	# post photon angle, previous basis pairs
	for i in range(len(output_items[0])):
		# set basis used for previous photon
		output_items[0][i] = self.sel_basis
		# randomly select a bit
        	r=random.randint(0, 1)
		# randomly select a basis
        	self.sel_basis = random.randint(0, 1)
		# set angle corresponding to "sel_basis" and "r"
		output_items[1][i] = self.basis[self.sel_basis][r]
		# memorize random bit
		self.key_bit.append(r)
	if self.debug_stderr: 
           sys.stderr.write("encoder.work():bases: " + \
                str(output_items[0]) + \
		" angles: " + str(output_items[1]) + "\n")
	# return number of posted pairs
	return len(output_items[0])
	

