# ---------------------------------------------------------------------------- #
#   Author:       tedpehanich                                                  #
#   Created:      10/7/2024, 8:22:30 PM                                        #
# ---------------------------------------------------------------------------- #

from vex import *

brain=Brain()


rpm1 = 0
rpm2 = 0
rpm3 = 0
rpm4 = 0


right_wheel_1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1)
right_wheel_2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1)
left_wheel_1 = Motor(Ports.PORT9, GearSetting.RATIO_6_1)
left_wheel_2 = Motor(Ports.PORT10, GearSetting.RATIO_6_1)

right_wheels = MotorGroup (right_wheel_1, right_wheel_2)
left_wheels = MotorGroup (left_wheel_1, left_wheel_2)
conveyer = Motor(Ports.PORT5, GearSetting.RATIO_18_1)
flex_wheels = Motor(Ports.PORT1, GearSetting.RATIO_18_1)

bradley_controller = Controller(ControllerType.PRIMARY)

bradley_controller_joystick_left = bradley_controller.axis2.position()
bradley_controller_joystick_right = bradley_controller.axis4.position()

def sprint():
    if bradley_controller_joystick_left>2 and bradley_controller.buttonL1.pressing:
        global rpm1
        rpm1 += 25
        max (rpm1, 550)
    
    if bradley_controller_joystick_right>2 and bradley_controller.buttonL1.pressing:
        global rpm2
        rpm2 += 25
        max (rpm2, 550)

def intake():
    if bradley_controller.buttonB.pressed and flex_wheels.velocity(RPM)>-5 and flex_wheels.velocity(RPM)<5:
        flex_wheels.spin(FORWARD, 20, RPM)
    if bradley_controller.buttonB.pressed and flex_wheels.velocity(RPM)>5 or flex_wheels.velocity(RPM)<-5:
        flex_wheels.stop()

def ring_riser():
    if bradley_controller.buttonA.pressed and conveyer.velocity(RPM)>-5 and conveyer.velocity(RPM)<5:
        conveyer.spin(FORWARD, 150, RPM)
    if bradley_controller.buttonA.pressed and conveyer.velocity(RPM)>5 or conveyer.velocity(RPM)<-5:
        conveyer.stop()

def drive():
    if bradley_controller_joystick_left>2:
        global rpm1
        rpm1 += 20
        max (rpm1, 400)

    if bradley_controller_joystick_right>2:
        global rpm2
        rpm2 += 20
        max (rpm2, 400)

    if bradley_controller_joystick_left<-2:
        global rpm3
        rpm3 += 20
    
    if bradley_controller_joystick_right<-2:
        global rpm4
        rpm4 += 20


    if rpm2 > rpm1:
        rpm1 = 0
    if rpm1 > rpm2:
        rpm2 = 0
    if rpm3 > rpm4:
        rpm4 = 0
    if rpm4 > rpm3:
        rpm3 = 0

while True:
   
    drive()
    sprint()
    intake()
    ring_riser()
    left_wheels.spin(FORWARD, rpm1, RPM)
    right_wheels.spin(FORWARD, rpm2, RPM)
    left_wheels.spin(REVERSE, rpm3, RPM)
    right_wheels.spin(REVERSE, rpm4, RPM)
    wait(5, MSEC)