# Software Defined Quantum Stream-Cipher for GNU Radio


```
The module implements the protocol originally described in: 

M. Barbeau, "Software Defined Quantum Stream-Cipher," GNU Radio Conference, Washington, DC (USA), August 2015.

See: http://people.scs.carleton.ca/~barbeau/Publications/2015/GNURadio_2015.pdf

```

# Copyright 2016 Michel Barbeau, Carleton University.
# Version: November 5, 2016

![Loopback Example](https://github.com/michelbarbeau/gr-quantomm/blob/master/sender.jpg)

## Installing

`git clone https://github.com/michelbarbeau/gr-quantomm`

## Building

```
cd gr-quantomm

mkdir build

cd build

cmake ../
 
make

sudo make install

sudo ldconfig
```

## Running

![Loopback Example](https://github.com/michelbarbeau/gr-quantomm/blob/master/simulation.png)


```
To run within gnuradio-companion

Open the flow graph  gr-quantomm/examples/simulation.grc.

To run outside gnuradio-companion

cd gr-quantomm/examples

python top_block.py

EXAMPLE

$ python top_block.py
encoder.work():len(input_items[0]): 4
encoder.work():bases: [0 0 1 0 1 1 0 1] angles: [ 90 135  90  45  45  90  45 135]
encoder.work():len(input_items[0]): 1
decoder.work():feedback: [0, 0, 1, 0, 0, 0, 1, 0]
encoder.work():bases: [1 0] angles: [90  0]
encoder.handle_msg():feedback: [0L, 0L, 1L, 0L, 0L, 0L, 1L, 0L]
encoder.handle_msg():plain text: [0, 1] cipher text: [1, 0]
decoder.work():feedback: [0, 0]
decoder.handle_msg():plain text: [0L, 1L] cipher text: [1L, 0L]
* MESSAGE DEBUG PRINT PDU VERBOSE *
()
pdu_length = 2
contents = 
0000: 00 01 
***********************************

```
