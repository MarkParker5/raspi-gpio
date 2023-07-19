try:
    import RPi.GPIO as GPIO
    from spidev import SpiDev
    is_mocked = False
except (RuntimeError, ModuleNotFoundError, ImportError):
    from . import GPIO_mock as GPIO
    from .spidev_mock import SpiDev
    is_mocked = True
    print('Warning: RPi.GPIO cannot be imported, using mock GPIO instead.')
