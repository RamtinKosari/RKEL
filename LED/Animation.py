# - Include LEDs Handler Module
from .LEDHandler import *

# - Include Animation Arrays
from .AnimationArrays import *

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
    def blink(self, delay = 0.001, times = 5, mode = 'serial', blink_array = AnimationArrays.Blink.Normal, array_reverse = False):
        # - Show Log
        printRKEL(RKEL_LABEL, "Blinking LEDs for {}{}{} Times with {}{}{} Seconds Delay in {}{}{} Mode ...".format(LIGHT_INFO, times, RESET, LIGHT_INFO, delay, RESET, LIGHT_INFO, mode, RESET), force = True)
        # - Check Reverse
        if array_reverse:
            blink_array = list(reversed(blink_array))
        # - Blink LEDs
        for _ in range(times):
            # - Check Mode
            if mode == 'serial':
                # - Serial Blinking
                for pin in self.leds.pins:
                    self.leds.on(pin)
                    time.sleep(delay)
                    self.leds.off(pin)
                    time.sleep(delay)
            elif mode == 'serial-forward-backward':
                # - Serial Forward Backward Blinking
                for pin in self.leds.pins:
                    self.leds.on(pin)
                    time.sleep(delay)
                    self.leds.off(pin)
                for pin in reversed(self.leds.pins):
                    self.leds.on(pin)
                    time.sleep(delay)
                    self.leds.off(pin)
            elif mode == 'parallel':
                # - Parallel Blinking
                for pin in self.leds.pins:
                    self.leds.on(pin)
                time.sleep(delay)
                for pin in self.leds.pins:
                    self.leds.off(pin)
                time.sleep(delay)
            elif mode == 'random':
                # - Random Blinking
                for _ in range(len(self.leds.pins)):
                    pin = random.choice(self.leds.pins)
                    self.leds.on(pin)
                    time.sleep(delay)
                    self.leds.off(pin)
                    time.sleep(delay)
            elif mode == 'blink-array':
                # - Blink Array
                for blink in blink_array:
                    for index in blink:
                        self.leds.on(self.leds.pins[index])
                    time.sleep(delay)
                    for index in blink:
                        self.leds.off(self.leds.pins[index])
                    time.sleep(delay)
            else:
                pass
    # - Fade Animation
    def fade(self, delay = 0.001, times = 5, mode = 'serial', fade_array = AnimationArrays.Fade.Normal, array_reverse = False, fade_step = 1):
        # - Show Log
        printRKEL(RKEL_LABEL, "Fading LEDs for {}{}{} Times with {}{}{} Seconds Delay in {}{}{} Mode ...".format(LIGHT_INFO, times, RESET, LIGHT_INFO, delay, RESET, LIGHT_INFO, mode, RESET), force = True)
        # - Check Reverse
        if array_reverse:
            fade_array = list(reversed(fade_array))
        # - Initialize Fade LEDs
        self.leds.pwm()
        # - Fade LEDs
        for _ in range(times):
            # - Check Mode
            if mode == 'fade-in':
                # - Fade In
                for fade in fade_array:
                    for index in fade:
                        for duty_cycle in range(0, 101, fade_step):
                            self.leds.PWM_LEDs[index].ChangeDutyCycle(duty_cycle)
                            time.sleep(delay)
            elif mode == 'fade-out':
                # - Fade Out
                for fade in fade_array:
                    for index in fade:
                        for duty_cycle in range(100, -1, -fade_step):
                            self.leds.PWM_LEDs[index].ChangeDutyCycle(duty_cycle)
                            time.sleep(delay)
            else:
                pass

    # - Wave Animation