# - Import RKEL Configurations
from Configs import *

# - LEDs Handler Class Definition
class LEDHandler:
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
            GPIO.output(pin, GPIO.LOW)
            # - Show Log
            printRKEL(RKEL_LABEL, SUCCESS, "LED Pin {}{}{} Initialized".format(LIGHT_INFO, pin, RESET), force = True)
    # - Method to Turn LED On
    def on(self, pin):
        GPIO.output(pin, GPIO.HIGH)
    # - Method to Turn LED Off
    def off(self, pin):
        GPIO.output(pin, GPIO.LOW)
            