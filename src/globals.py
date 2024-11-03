from vex import *


right_wheels = MotorGroup (Ports.PORT11, GearSetting.RATIO_6_1, Ports.PORT12, GearSetting.RATIO_6_1)
left_wheels = MotorGroup (Ports.PORT9, GearSetting.RATIO_6_1, Ports.PORT10, GearSetting.RATIO_6_1)
conveyer = Motor(Ports.PORT5, GearSetting.RATIO_18_1)
flex_wheels = Motor(Ports.PORT1, GearSetting.RATIO_18_1)

bradley_controller = Controller(ControllerType.PRIMARY)

bradley_controller_joystick_left = bradley_controller.axis2.position()
bradley_controller_joystick_right = bradley_controller.axis4.position()

#jsfgsdjkhf