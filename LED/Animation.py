# - Include LEDs Handler Module
from .LEDHandler import *

# - Animation Class Definition
class Animation:
    # - Method to Initialize Animation
    def __init__(self, pins):
        self.leds = LEDHandler(pins)
    # - Clear LEDs
    def clear(self):
        # - Turn Off All LEDs
        for pin in self.leds.pins:
            self.leds.off(pin)
        # - Cleanup GPIO Settings
        GPIO.cleanup()
    # - Blink Animation
    def blink(self, delay = 0.001, times = 5, mode = 'serial'):
        for _ in range(times):
            # - Check Mode
            if mode == 'serial':
                # - Serial Blinking
                for pin in self.leds.pins:
                    self.leds.on(pin)
                    time.sleep(delay)
                    self.leds.off(pin)
                    time.sleep(delay)
            elif mode == 'parallel':
                # - Parallel Blinking
                for pin in self.leds.pins:
                    self.leds.on(pin)
                time.sleep(delay)
                for pin in self.leds.pins:
                    self.leds.off(pin)
                time.sleep(delay)
            else:
                pass
        # - Clear LEDs
        self.clear()