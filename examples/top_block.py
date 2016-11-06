#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Nov  5 19:51:03 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import quantomm


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Blocks
        ##################################################
        self.quantomm_encoder_0 = quantomm.encoder(True)
        self.quantomm_decoder_0 = quantomm.decoder(True)
        self.quantomm_channel_ii_1 = quantomm.channel_ii()
        self.quantomm_channel_ii_0 = quantomm.channel_ii()
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 5)), False)
        self.Message_Debug_Out_Plain_Text = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.quantomm_decoder_0, 'plaintext'), (self.Message_Debug_Out_Plain_Text, 'print_pdu'))    
        self.msg_connect((self.quantomm_decoder_0, 'feedback'), (self.quantomm_encoder_0, 'feedback'))    
        self.msg_connect((self.quantomm_encoder_0, 'ciphertext'), (self.quantomm_decoder_0, 'ciphertext'))    
        self.connect((self.analog_random_source_x_0, 0), (self.quantomm_encoder_0, 0))    
        self.connect((self.quantomm_channel_ii_0, 0), (self.quantomm_decoder_0, 0))    
        self.connect((self.quantomm_channel_ii_1, 0), (self.quantomm_decoder_0, 1))    
        self.connect((self.quantomm_encoder_0, 0), (self.quantomm_channel_ii_0, 0))    
        self.connect((self.quantomm_encoder_0, 1), (self.quantomm_channel_ii_1, 0))    


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
