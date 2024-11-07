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

goal_lock_piston = DigitalOut(brain.three_wire_port.a)
goal_lock_piston.set(True)

right_wheel_1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1)
right_wheel_2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1)
left_wheel_1 = Motor(Ports.PORT9, GearSetting.RATIO_6_1)
left_wheel_2 = Motor(Ports.PORT10, GearSetting.RATIO_6_1)

right_wheels = MotorGroup (right_wheel_1, right_wheel_2)
left_wheels = MotorGroup (left_wheel_1, left_wheel_2)
conveyer = Motor(Ports.PORT20, GearSetting.RATIO_18_1)
flex_wheels = Motor(Ports.PORT1, GearSetting.RATIO_18_1)

bradley_controller = Controller(ControllerType.PRIMARY)

bradley_controller_joystick_left = bradley_controller.axis2.position()
bradley_controller_joystick_right = bradley_controller.axis4.position()

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

def goal_lock():
    if bradley_controller.buttonR1.pressed:
        goal_lock_piston.set(False)

    if bradley_controller.buttonR2.pressed:
        goal_lock_piston.set(True)

def drive():

    if bradley_controller_joystick_left>2:
        global rpm1
        rpm1 += 20
        rpm1 = min (rpm1, 400)

    if bradley_controller_joystick_right>2:
        global rpm2
        rpm2 += 20
        rpm2 = min (rpm2, 400)

    if bradley_controller_joystick_left<-2:
        global rpm3
        rpm3 += 20
        rpm3 = min (rpm3, 400)
    
    if bradley_controller_joystick_right<-2:
        global rpm4
        rpm4 += 20
        rpm4 = min (rpm4, 400)

def sprint():
    if bradley_controller_joystick_left>2 and bradley_controller.buttonL1.pressing:
        global rpm1
        rpm1 += 25
        rpm1 = min (rpm1, 570)
    
    if bradley_controller_joystick_right>2 and bradley_controller.buttonL1.pressing:
        global rpm2
        rpm2 += 25
        rpm2 = min (rpm2, 570)

    if bradley_controller_joystick_left<-2 and bradley_controller.buttonL1.pressing:
        global rpm3
        rpm3 += 25
        rpm3 = min (rpm3, 570)
    
    if bradley_controller_joystick_right<-2 and bradley_controller.buttonL1.pressing:
        global rpm4
        rpm4 += 25
        rpm4 = min (rpm4, 570)

def stop():
    if bradley_controller_joystick_left >-5 and bradley_controller_joystick_left<5:
        global rpm1
        global rpm3

        rpm1 = 0
        rpm3 = 0

    if bradley_controller_joystick_right >-5 and bradley_controller_joystick_right<5:
        global rpm2
        global rpm4

        rpm2 = 0
        rpm4 = 0


    if rpm3 > rpm1:
        rpm1 =0
    if rpm4 > rpm2:
        rpm2 =0
    if rpm2 > rpm4:
        rpm4 =0
    if rpm1 > rpm3:
        rpm3 =0


    if rpm1 < 0:
        rpm1 = 0
    if rpm2 < 0:
        rpm2 = 0
    if rpm3 < 0:
        rpm3 = 0
    if rpm4 < 0:
        rpm4 = 0

    if rpm1 > 600:
        rpm1 = 570
    if rpm2 > 600:
        rpm2 = 570
    if rpm3 > 600:
        rpm3 = 570
    if rpm4 > 600:
        rpm4 = 570



while True:
   
    drive()
    sprint()
    intake()
    ring_riser()
    goal_lock()
    stop()

    left_wheels.spin(FORWARD, rpm1, RPM)
    right_wheels.spin(FORWARD, rpm2, RPM)
    left_wheels.spin(REVERSE, rpm3, RPM)
    right_wheels.spin(REVERSE, rpm4, RPM)

    wait(5, MSEC)