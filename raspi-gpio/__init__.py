try:
    from RPi.GPIO import *
except (RuntimeError, ModuleNotFoundError, ImportError):
    from .GPIO import *
