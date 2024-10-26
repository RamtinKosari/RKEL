from LED.Animation import *

if __name__ == '__main__':
    # - Initialize Animation
    animation = Animation([4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26])
    # - Blink Animation
    animation.blink(0.04, 1, 'blink-array', AnimationArrays.Blink.Incremental)
    # - Clear LEDs
    animation.clear()