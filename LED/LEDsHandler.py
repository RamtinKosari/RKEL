# - Include LED Handler Module
from LEDHandler import *

# - LEDs Handler Class Definition
class LEDsHandler:
    def __init__(self, pins):
        # - Setup GPIO Mode
        GPIO.setmode(GPIO.BCM)
        # - Set LED Pins
        self.pins = pins
        # - Initialize GPIO Pins
        for pin in self.pins:
            # - Setup GPIO Pin
            GPIO.setup(pin, GPIO.OUT)
            # - Set LED State
            GPIO.output(self.pin, GPIO.LOW)
            # - Show Log
            printRKEL(RKEL_LABEL, SUCCESS, "LED Pin {}{}{} Initialized".format(LIGHT_INFO, pin, RESET), force = True)
            