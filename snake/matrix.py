"""
    Copyright 2015 Nashwan Azhari, Krody Robert.
    Licensed under the GPLv2 license. See LICENSE file for details.
"""
import sys
from snake.color import Color

try:
    from spidev import SpiDev
except ImportError as e:
    print("Failed to import SPI library:", e)
    sys.exit(-1)


class Matrix(object):
    """
        The class which models the operation of the Olimex 8x8 RGB LED matrix.
        The numbering scheme used when defining the pins are with respect to
        the BCM numbering scheme.

        Wiring:
            - VCC = driving voltage for the matrix. 5 volts.
            - GND = ground connection from the matrix.
            - DIN = data in for the matrix, GPIO pin 10 (SPI MOSI).
            - CS = chip select, depending on SPI channel selection.
            - CLK = serial clock, GPIO pin 11 (SPI SCK).

    """

    def __init__(self, spi_device=0):
        """
            Basic constructor for our driver class.

            @param: spi_device - the SPI device to be used.
                Acts as a chip-enable. The Raspberry PI B+ has two such device
                output pins in-built.
                Defaults to 0.

            @return: None
        """
        if spi_device != 1:
            spi_device = 0

        self.__spi = SpiDev()
        self.__spi.mode = 0b01
        self.__spi.open(0, spi_device)

        self.__buffer = [0] * 24

    def draw_pixel(self, pixel):
        """
            Draws a given Pixel object to the internal buffer.
            The buffer is formed of 24 bytes.
            Each byte represents a single color, the n'th bit being whether
            that particular color is active in the n'th led of that row.
            The colors are ordered in reverse. (BGR).

            @param: pixel - a Pixel object.

            @return: the Pixel encoded as a byte.
        """
        # current row we're on:
        row = 3 * pixel.y

        # clear currently present color by unsetting the corresponding bit from
        # the three color bytes:
        self.__buffer[row] &= ~(1 << pixel.x)  # clear red.
        self.__buffer[row + 1] &= ~(1 << pixel.x)  # clear green.
        self.__buffer[row + 2] &= ~(1 << pixel.x)  # clear blue.

        # set red bit for this pixel, if necessary:
        if pixel.color in [Color.red, Color.white, Color.brown, Color.purple]:
            self.__buffer[row] |= 1 << pixel.x
        # set green bit:
        if pixel.color in [Color.green, Color.white, Color.turquoise, Color.brown]:
            self.__buffer[row + 1] |= 1 << pixel.x
        # set blue bit:
        if pixel.color in [Color.blue, Color.white, Color.turquoise, Color.purple]:
            self.__buffer[row + 2] |= 1 << pixel.x

    def write(self):
        """
            Serially writes the whole of the video buffer to the matrix.
        """
        self.__spi.xfer(self.__buffer)

    def clear(self):
        """
            Clears both the internal buffer and the matrix.
        """
        self.__buffer = [0] * 24
        self.write()

    def cleanup(self):
        """
            Clears all registers and terminates the SPI connection.
        """
        self.clear()
        self.__spi.close()

