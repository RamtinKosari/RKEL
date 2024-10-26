# - Include LEDs Handler Module
from LEDsHandler import *

# - Animation Class Definition
class Animation:
    # - Method to Initialize Animation
    def __init__(self, pins):
        self.leds = LEDsHandler(pins)
    # - Blink Animation
    @staticmethod
    def blink(delay = 0.001):
        pass