from random import randint

   
HIGH = 1
LOW = 0
IN = 1
OUT = 0
HARD_PWM = 43
I2C = 42
SPI = 41
SERIAL = 40
UNKNOWN = -1
BOARD = 10
BCM = 11
PUD_OFF = 0
PUD_UP = 2
PUD_DOWN = 1
RISING = 0
FALLING = 0
BOTH = 0
RPI_REVISION = 0

class PWM(object):

    def __init__(self, channel, frequency):
        pass

    def start(self, dutycycle):
        pass

    def ChangeDutyCycle(self, dutycycle):
        pass

    def ChangeFrequency(self, frequency):
        pass

    def stop(self):
        pass

def cleanup(channel=None):
    pass

def setup(channel, direction, initial=0, pull_up_down=PUD_OFF):
    pass

def output(channel, value):
    pass

def input(channel):
    return randint(0, 1)

def setmode(mode):
    pass

def getmode(self):
    return self.BCM

def add_event_callback(gpio, callback):
    pass

def add_event_detect(gpio, edge, callback=None, bouncetime=None):
    pass

def remove_event_detect(gpio):
    pass

def event_detected(channel):
    return False

def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
    pass

def gpio_function(channel):
    return OUT

def setwarnings(state):
    pass

def pulseOut(ce_pin, value, period):
    pass
