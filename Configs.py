# - Import Necessary Libraries
import RPi.GPIO as GPIO
import time

BOARD_MODELS = [
    'Raspberry Pi 4',
]

# - Show RKEL Logs
SHOW_RKEL_LOGS = True

# - Reset Color
RESET = f'\033[0m'
# - Error Color
ERR = f'\033[38;2;255;200;0m'
# - Info Color
INFO = f'\033[38;2;106;140;150m'
# - Error Info Color
ERROR_INFO = f'\033[38;2;210;153;192m'
# - Light Info Color
LIGHT_INFO = f'\033[38;2;106;106;150m'
# - Failed Terminal Output
FAILED = f'\033[38;2;255;0;0m[FAILED]\033[0m'
# - Success Terminal Output
SUCCESS = f'\033[38;2;0;255;0m[SUCCESS]\033[0m'
# - Warning Terminal Output
WARNING = f'\033[38;2;255;255;0m[WARNING]\033[0m'
# - Debug Terminal Output
DEBUG_INFO = f'\033[38;2;237;109;0m[DEBUG]\033[0m'
# - Database Terminal Output
RKEL_LABEL = f'\033[38;2;150;180;180m[RKEL]\033[0m'

# - Method to Print Database Handler Logs
def printRKEL(*__input, **kargs):
    # - Check if force = True has been Passed
    if "force" in kargs:
        if kargs["force"] == True:
            # - Print Current Date and Time
            print(INFO + "(" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ")", end = ' ', flush = True)
            # - Check Parameters
            for arg in __input:
                print(arg, end = ' ', flush = True)
            # - Print New Line
            print()
            return
    # - Check if Logs are Enabled
    if SHOW_RKEL_LOGS == False:
        return
    # - Print Current Date and Time
    print(INFO + "(" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ")", end = ' ', flush = True)
    # - Check Parameters
    for arg in __input:
        print(arg, end = ' ', flush = True)
    # - Print New Line
    print()
    return