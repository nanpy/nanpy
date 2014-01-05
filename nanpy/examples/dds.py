from nanpy.ad9850 import AD9850
from nanpy.serialmanager import SerialManager

# http://nr8o.dhlpilotcentral.com/?p=83
W_CLK = 'A5'  # Pin 8 - connect to AD9850 module word load clock pin (CLK)
FQ_UD = 'A4'  # Pin 9 - connect to freq update pin (FQ)
DATA = 'A3'  # Pin 10 - connect to serial data load pin (DATA)
RESET = 'A2'  # Pin 11 - connect to reset pin (RST).

F = 440  # Hz


def dds():
    connection = SerialManager()
    dds = AD9850([W_CLK, FQ_UD, DATA, RESET], connection=connection)

    dds.setup()
    dds.write_frequency(F)


if __name__ == '__main__':
    dds()
