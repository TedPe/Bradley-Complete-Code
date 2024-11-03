# ├──── main.py 
# ---------------------------------------------------------------------------- #
#   Author:       tedpehanich                                                  #
#   Created:      10/7/2024, 8:22:30 PM                                        #
# ---------------------------------------------------------------------------- #

from vex import *
# ├──── globals.py 


right_wheels = MotorGroup (Ports.PORT11, GearSetting.RATIO_6_1, Ports.PORT12, GearSetting.RATIO_6_1)
left_wheels = MotorGroup (Ports.PORT9, GearSetting.RATIO_6_1, Ports.PORT10, GearSetting.RATIO_6_1)
conveyer = Motor(Ports.PORT5, GearSetting.RATIO_18_1)
flex_wheels = Motor(Ports.PORT1, GearSetting.RATIO_18_1)

bradley_controller = Controller(ControllerType.PRIMARY)

bradley_controller_joystick_left = bradley_controller.axis3.position()
bradley_controller_joystick_right = bradley_controller.axis2.position()

#jsfgsdjkhf
# ├──── / globals.py >


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
        flex_wheels.spin(FORWARD)
    if bradley_controller.buttonA.pressed:
        flex_wheels.stop()

def ring_riser():
    if bradley_controller.buttonA.pressed:
       
        conveyer.spin(FORWARD)
    elif bradley_controller.buttonA.pressed:
        
        conveyer.spin(FORWARD)

def drive():
    while True:
        if bradley_controller_joystick_left>0:
            left_wheels.spin(FORWARD, 80)
            #wait (20, MSEC)
            #left_wheels.spin(FORWARD, 0)
        if bradley_controller_joystick_right>0:
            right_wheels.spin(FORWARD, 80)
            #wait (20, MSEC)
            #right_wheels.spin(FORWARD, 0)

        if bradley_controller_joystick_left<0:
            left_wheels.spin(REVERSE, 80)
            #wait (20, MSEC)
            #left_wheels.spin(REVERSE, 0)
        if bradley_controller_joystick_right<0:
            right_wheels.spin(REVERSE, 80)
            #wait (20, MSEC)
            #right_wheels.spin(REVERSE, 0)
        wait (20,MSEC)
        brain.screen.print_at(bradley_controller_joystick_left, x=200, y =200, )

   
new = Thread(drive)    
    #sprint()
    #intake()
    #ring_riser()
    #wait(10, MSEC)
# ├──── / main.py >
