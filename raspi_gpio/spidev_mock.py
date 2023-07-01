class SpiDev:

    bits_per_word = 8
    cshigh = False
    loop = False
    lsbfirst = False
    max_speed_hz = 125000000
    mode = 0
    threewire = False
    no_cs = False

    def __init__(self, bus=0, cs=0):
        pass

    def open(self, bus, cs):
        pass

    def close(self):
        pass

    def fileno(self):
        pass

    def readbytes(self, length):
        return []

    def writebytes(self,values):
        pass

    def writebytes2(self,values):
        pass

    def xfer(self, values, speed=4096, delay=0, bits=8):
        pass

    def xfer2(self, values, speed=4096, delay=0, bits=8):
        return [0] * 255

    def xfer3(self, values, speed=4096, delay=0, bits=8):
        pass
