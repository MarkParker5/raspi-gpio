<!-- coffee -->
<a href="https://buymeacoffee.com/markparker5" target="_blank">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://markparker.me/banners/coffee-dark.webp"
    />
    <img
      alt="Did this solve your problem? If it saved your time, you owe me a coffee"
      src="https://markparker.me/banners/coffee-light.webp"
    />
  </picture>
</a>

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
