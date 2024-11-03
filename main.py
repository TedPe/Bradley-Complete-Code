# ---------------------------------------------------------------------------- #
#   Author:       tedpehanich                                                  #
#   Created:      10/7/2024, 8:22:30 PM                                        #
# ---------------------------------------------------------------------------- #

from vex import *

brain=Brain()

right_wheel_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1)
right_wheel_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1)
left_wheel_1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1)
left_wheel_2 = Motor(Ports.PORT4, GearSetting.RATIO_18_1)

right_wheels = MotorGroup (right_wheel_1, right_wheel_2)
left_wheels = MotorGroup (left_wheel_1, left_wheel_2)
conveyer = Motor(Ports.PORT5, GearSetting.RATIO_18_1)
flex_wheels = Motor(Ports.PORT6, GearSetting.RATIO_18_1)

bradley_controller = Controller(ControllerType.PRIMARY)

bradley_controller_joystick_left = bradley_controller.axis2.position()
bradley_controller_joystick_right = bradley_controller.axis4.position()

def sprint():
    if bradley_controller_joystick_left>2 and bradley_controller.buttonL1.pressing:
        left_wheels.spin(FORWARD, 120, RPM)
    if bradley_controller.buttonL1.released:
        (left_wheels.stop)
    
    if bradley_controller_joystick_right>2 and bradley_controller.buttonL1.pressing:
        right_wheels.spin(FORWARD, 120, RPM)
    if bradley_controller.buttonL2.released:
        (right_wheels.stop)

def intake():
    if bradley_controller.buttonB.pressed and flex_wheels.velocity(RPM)>-5 and flex_wheels.velocity(RPM)<5:
        flex_wheels.spin(FORWARD, RPM, 20)
    if bradley_controller.buttonB.pressed and flex_wheels.velocity(RPM)>5 or flex_wheels.velocity(RPM)<-5:
        flex_wheels.stop()

def ring_riser():
    if bradley_controller.buttonA.pressed and conveyer.velocity(RPM)>-5 and conveyer.velocity(RPM)<5:
        conveyer.spin(FORWARD, 20, RPM)
    if bradley_controller.buttonA.pressed and conveyer.velocity(RPM)>5 or conveyer.velocity(RPM)<-5:
        conveyer.stop()

def drive():
    if bradley_controller_joystick_left>2:
        left_wheels.spin(FORWARD, 80, RPM)
        wait (5, MSEC)
        left_wheels.stop()
    if bradley_controller_joystick_right>2:
        right_wheels.spin(FORWARD, 80, RPM)
        wait (5, MSEC)
        right_wheels.stop()

    if bradley_controller_joystick_left<-2:
        left_wheels.spin(REVERSE, 80, RPM)
        wait (5, MSEC)
        left_wheels.stop()
    if bradley_controller_joystick_right<-2:
        right_wheels.spin(REVERSE, 80, RPM)
        wait (5, MSEC)
        right_wheels.stop()

while True:
   
    drive()
    sprint()
    intake()
    ring_riser()
    wait(5, MSEC)