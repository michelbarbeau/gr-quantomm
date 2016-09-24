# Software Defined Quantum Stream-Cipher for GNU Radio


The module implements the protocol originally described in: 

M. Barbeau, "Software Defined Quantum Stream-Cipher," GNU Radio Conference, Washington, DC (USA), August 2015.

See: http://people.scs.carleton.ca/~barbeau/Publications/2015/GNURadio_2015.pdf

# Copyright 2016 Michel Barbeau, Carleton University.
# Version: September 23, 2016

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
```

## Running

To run within gnuradio-companion

Open the flow graph  gr-quantomm/examples/simulation.grc.

To run outside gnuradio-companion

cd gr-quantomm/examples

python top_block.py
