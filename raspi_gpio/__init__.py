try:
    from RPi.GPIO import *
    import spidev
except (RuntimeError, ModuleNotFoundError, ImportError):
    from .GPIO import *
    from .spidev import *
    print('Warning: RPi.GPIO cannot be imported, using mock GPIO instead.')
