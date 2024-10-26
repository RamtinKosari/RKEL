from LED.Animation import *
from Rotor.RotorHandler import *

if __name__ == '__main__':
    # # - Initialize Animation
    # animation = Animation([4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26])
    # # - Blink Animation
    # # animation.blink(0.04, 1, 'blink-array', AnimationArrays.Blink.Scan)
    # animation.fade(0.04, 1, 'fade-out', AnimationArrays.Fade.Wave)
    # # - Clear LEDs
    # animation.clear()


    # - Initialize Rotor Handler
    rotor = RotorHandler()
    rotor.power(20)