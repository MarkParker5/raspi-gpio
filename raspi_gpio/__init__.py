try:
    from RPi.GPIO import *
    from spidev import *
except (RuntimeError, ModuleNotFoundError, ImportError):
    from .GPIO import *
    from .spidev import *
    print('Warning: RPi.GPIO cannot be imported, using mock GPIO instead.')
