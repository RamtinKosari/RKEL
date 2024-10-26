# - Import RKEL Configurations
from Configs import *

# - LEDs Handler Class Definition
class LEDHandler:
    def __init__(self, pins):
        # - Setup GPIO Mode
        GPIO.setmode(GPIO.BCM)
        # - Set LED Pins
        self.pins = pins
        # - Set PWM LEDs
        self.PWM_LEDs = []
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
    # - Method to Initialize PWM LEDs
    def pwm(self):
        self.PWM_LEDs = [GPIO.PWM(pin, 50) for pin in self.pins]
        for pwm_leds in self.PWM_LEDs:
            pwm_leds.start(0)
