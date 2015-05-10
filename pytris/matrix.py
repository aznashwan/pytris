'''
    Copyright 2015 Nashwan Azhari, Krody Robert.
    Licensed under the GPLv2 license. See LICENSE file for details.
'''
import sys
from color import Color

try:
    import spidev
except ImportError as e:
    print("Failed to import SPI library:", e)
    sys.exit(-1)

class Matrix(object):
    '''
        The class which models the operation of the Olimex 8x8 RGB LED matrix.
        The numbering scheme used when defining the pins are with respect to
        the BCM numbering scheme.

        Wiring:
            - VCC = driving voltage for the matrix. 5 volts.
            - GND = ground connection from the matrix.
            - DIN = data in for the matrix, GPIO pin 10 (SPI MOSI).
            - CS = chip select, depending on SPI channel selection.
            - CLK = serial clock, GPIO pin 11 (SPI SCK).

    '''
    def __init__(self, spidevice=0):
        '''
            Basic constructor for our driver class.

            @param: spidevice - the SPI device to be used.
                Acts as a chip-enable. The Raspberry PI B+ has two such device
                output pins in-built.
                Defaults to 0.

            @return: None
        '''
        if spidevice != 1:
            spidevice = 0

        self.__spi = spidev.SpiDev()
        self.__spi.bits_per_word = 8
        self.__spi.mode = 0b01
        spidev.open(0, spidev)

        self.__buffer = bytearray([0] * 24)

    def clear(self):
        '''
            Clears both the internal buffer and the matrix.
        '''
        self.__buffer = bytearray([0] * 24)
        self.write()

    def drawpixel(self, pixel):
        '''
            Draws a given Pixel object to the internal buffer.
            The buffer is formed of 24 bytes. Each 3 bytes represents the
            coloring of the pixel on that particular row/column.

            @param: pixel - a Pixel object.

            @return: the Pixel encoded as a byte.
        '''
        # coordinates of the byte containing the pixel:
        row = 3 * pixel.y
        column = pixel.x / 8

        # clear currently present color:
        self.__buffer[row + column] &= ~(1 << pixel.x)
        self.__buffer[row + column + 1] &= ~(1 << pixel.x)
        self.__buffer[row + column + 2] &= ~(1 << pixel.x)

        # configure new color:
        if pixel.color & Color.blue:
            self.__buffer[row + column] |= 1 << pixel.x
        if pixel.color & Color.green:
            self.__buffer[row + column + 1] |= 1 << pixel.y
        if pixel.color & Color.red:
            self.__buffer[row + column + 2] |= 1 << pixel.y

    def write(self):
        '''
            Serially writes the whole of the video buffer to the matrix.
        '''
        self.__spi.xfer(self.__buffer, delay=10)

