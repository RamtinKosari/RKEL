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
    rotor = RotorHandler(4)
    rotor.power(20)
    time.sleep(1)
    rotor.power(30)
    time.sleep(1)
    rotor.power(40)
    time.sleep(1)
    rotor.power(50)
    time.sleep(1)
    rotor.power(60)
    time.sleep(1)
    rotor.power(70)
    time.sleep(1)
    rotor.power(80)
    time.sleep(1)
    rotor.power(90)
    time.sleep(1)
    rotor.power(100)
    time.sleep(3)
    rotor.cleanup()