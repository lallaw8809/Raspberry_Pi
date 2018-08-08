# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# MCP3008 VDD to Raspberry Pi 3.3V
# MCP3008 VREF to Raspberry Pi 3.3V
# MCP3008 AGND to Raspberry Pi GND
# MCP3008 DGND to Raspberry Pi GND
# MCP3008 CLK to Raspberry Pi pin 18
# MCP3008 DOUT(MISO) to Raspberry Pi pin 23
# MCP3008 DIN(MOSI) to Raspberry Pi pin 24
# MCP3008 CS/SHDN to Raspberry Pi pin 25


# Software SPI configuration:
# Use this hardware connection for RPi3
# CLK  = 23
# MISO = 21
# MOSI = 19
# CS   = 24
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)


