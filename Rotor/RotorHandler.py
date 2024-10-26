# - Import RKEL Configurations
from Configs import *

# - RotorHandler Class Definition
class RotorHandler:
    # - Method to Initialize Rotor Handler
    def __init__(self, pin):
        # - Setup GPIO Mode
        GPIO.setmode(GPIO.BCM)
        # - Set Rotor Pin
        self.pin = pin
        # - Set PWM Rotor
        self.PWM_ROTOR = None
        # - Setup GPIO Pin
        GPIO.setup(pin, GPIO.OUT)
        # - Set LED State
        GPIO.output(pin, GPIO.LOW)
        # - Initialize PWM Rotor
        self.PWM_ROTOR = GPIO.PWM(self.pin, 100)
        # - Start PWM Rotor at 0 Duty Cycle
        self.PWM_ROTOR.start(0)
        # - Show Log
        printRKEL(RKEL_LABEL, SUCCESS, "Rotor Pin {}{}{} Initialized".format(LIGHT_INFO, pin, RESET), force = True)
    # - Method to Cleanup Rotor Handler
    def cleanup(self):
        # - Set PWM Rotor at 0 Duty Cycle
        self.PWM_ROTOR.ChangeDutyCycle(0)
        # - Stop PWM Rotor
        self.PWM_ROTOR.stop()
        # - Cleanup GPIO Settings
        GPIO.cleanup()
        # - Show Log
        printRKEL(RKEL_LABEL, SUCCESS, "Rotor Pin {}{}{} Cleaned Up".format(LIGHT_INFO, self.pin, RESET), force = True)
    # - Method to Power Rotor
    def power(self, percentage: int):
        # - Show Log
        printRKEL(RKEL_LABEL, "Powering Rotor at {}{}{}% ...".format(LIGHT_INFO, percentage, RESET), force = True)
        # - Set Duty Cycle
        self.PWM_ROTOR.ChangeDutyCycle(100)