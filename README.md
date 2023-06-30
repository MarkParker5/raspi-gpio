# raspi-gpio
RPi.GPIO and spidev wrapper with mocks for developmennt on any platform

# Installation
```sh
pip install raspi-gpio
```

# Usage
Replace
```python
import RPi.GPIO as GPIO
from spidev import SpiDev
```
with
```python
from raspi_gpio import GPIO, SpiDev
```
