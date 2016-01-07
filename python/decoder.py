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
from operator import xor
import pmt # polymorphic data types
import sys

class decoder(gr.sync_block):
    "Quantum decoder"
    # debug mode flag
    debug_stderr=True
    # rectilinear basis & diagonal basis angles
    basis = [[0, 90], [45, 135]]
    # received key bit buffer
    key_bit = []
    # selected random basis
    sel_basis = -1  # first item is not used, set to impossible to match value
    # decoded bit
    dec_bit = 0

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name = "decoder",
            # input signature
	    # in port of photon angles: 0s, 90s, 45s and 135s 
            in_sig = [numpy.uint32,
	    # in port of selected bases: 0s and 1s
		      numpy.uint32],
	    # output signature
            out_sig = None)
	# asynchronous encrypted in data port, 0s and 1s
 	self.message_port_register_in(pmt.intern('ciphertext'))
        self.set_msg_handler(pmt.intern('ciphertext'), self.handle_msg)
	# asynchronous to-encoder feedback port, 0s (neg.) and 1s (pos.) 
 	self.message_port_register_out(pmt.intern('feedback'))
	# asynchronous out port for plain text 
 	self.message_port_register_out(pmt.intern('plaintext'))

    # from-encoder encrypted data port handler
    def handle_msg(self, msg):
        # decrypted data
        plaintext = []
        # consume encrypted data from encoder
	ciphertext = pmt.to_python(msg)
	for i in range(len(ciphertext)):
		# use one key bit
		k = self.key_bit.pop(0)
                # post decrypted data bit
                t = ciphertext[i]^k
                plaintext.append(t)
	if self.debug_stderr: 
           sys.stderr.write("decoder.handle_msg():plain text: " + \
                str(plaintext) + \
		" cipher text: " + str(ciphertext) + "\n")
        # post encrypted data, converted to the PDU PMT  
        self.message_port_pub(pmt.intern('plaintext'), \
            pmt.cons(pmt.to_pmt({}), \
                pmt.init_u32vector(len(plaintext),plaintext)))

    def work(self, input_items, output_items):
	# feedback to encoder
	feedback = []
	# read photon angle, previous basis pairs
	for i in range(len(input_items[0])):
		# compares encoder and decoder basis used for previous photon
		if input_items[0][i]==self.sel_basis:
			# append positive feedback
			feedback.append(1)
			# append corresponding biy to key
			self.key_bit.append(self.dec_bit)
		else:
			# append negative feedback
			feedback.append(0)

		# randomly select a basis
        	self.sel_basis=random.randint(0, 1)
		# decode a photon
		if input_items[1][i]==self.basis[self.sel_basis][0]:
			# store a zero
			self.dec_bit = 0
		elif input_items[1][i]==self.basis[self.sel_basis][1]:
			# store a one
			self.dec_bit = 1
		else:
			# store a random value
			self.dec_bit = random.randint(0, 1)
        # post feedback to encoder
        self.message_port_pub(pmt.intern('feedback'), 
		pmt.to_pmt(feedback)) 
	return len(input_items[0])


