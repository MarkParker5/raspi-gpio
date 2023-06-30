try:
    from RPi.GPIO import *
except (RuntimeError, ModuleNotFoundError, ImportError):
    from .GPIO import *
    print('Warning: RPi.GPIO cannot be imported, using mock GPIO instead.')
