# - Import RKEL Configurations
from Configs import *

# - LED Handler Class Definition
class LEDHandler:
    # - Method to Initialize LED Handler
    def __init__(self, pin, model = 'Raspberry Pi'):
        # - Set Pin Number
        self.pin = pin
    # - Method to Turn LED On
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    # - Method to Turn LED Off
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)