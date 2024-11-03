# ---------------------------------------------------------------------------- #
#   Author:       tedpehanich                                                  #
#   Created:      10/7/2024, 8:22:30 PM                                        #
# ---------------------------------------------------------------------------- #

from vex_tests import *
from globals import *


brain=Brain()

        


def sprint():
    if bradley_controller_joystick_left>52 and bradley_controller.buttonL1.pressing:
        left_wheels.spin(FORWARD, 120)
        bradley_controller.buttonL1.released (left_wheels.stop)
    
    if bradley_controller_joystick_right>52 and bradley_controller.buttonL2.pressing:
        right_wheels.spin(FORWARD, 120)
        bradley_controller.buttonL2.released (right_wheels.stop)

def intake():
    if bradley_controller.buttonB.pressed:
        flex_wheels.spin(FORWARD, RPM, 20)
    elif bradley_controller.buttonB.pressed:
        flex_wheels.spin(FORWARD, RPM, 0)

def ring_riser():
    if bradley_controller.buttonA.pressed:
        conveyer.spin(FORWARD, RPM, 20)
    elif bradley_controller.buttonA.pressed:
        conveyer.spin(FORWARD, RPM, 0)

def drive():
    if bradley_controller_joystick_left>52:
        left_wheels.spin(FORWARD, 80)
        wait (duration=20)
        left_wheels.spin(FORWARD, 0)
    if bradley_controller_joystick_right>52:
        right_wheels.spin(FORWARD, 80)
        wait (duration=20)
        right_wheels.spin(FORWARD, 0)

    if bradley_controller_joystick_left<48:
        left_wheels.spin(REVERSE, 80)
        wait (duration=20)
        left_wheels.spin(REVERSE, 0)
    if bradley_controller_joystick_right<48:
        right_wheels.spin(REVERSE, 80)
        wait (duration=20)
        right_wheels.spin(REVERSE, 0)

while True:
   
    drive()
    #sprint()
    #intake()
    #ring_riser()
    wait(10, MSEC)