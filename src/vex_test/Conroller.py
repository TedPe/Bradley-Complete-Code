class Controller:
    class Axis:
        def __init__(self, name):
            self.name = name
            self.position = 0  # Position of the joystick axis, from -100 to 100
            
        def set_position(self, position):
            """Simulate setting the joystick position."""
            if -100 <= position <= 100:
                self.position = position
            print(f"{self.name} position set to {self.position}")
        
        def get_position(self):
            """Get the current position of the joystick axis."""
            print(f"{self.name} position is {self.position}")
            return self.position

    class Button:
        def __init__(self, name):
            self.name = name
            self.pressed = False  # True if the button is pressed, False otherwise

        def press(self):
            """Simulate pressing the button."""
            self.pressed = True
            print(f"{self.name} button pressed")

        def release(self):
            """Simulate releasing the button."""
            self.pressed = False
            print(f"{self.name} button released")

        def is_pressed(self):
            """Return the button's current state."""
            print(f"{self.name} button is {'pressed' if self.pressed else 'released'}")
            return self.pressed

    def __init__(self):
        # Define the controller's joysticks (axes) and buttons
        self.Axis1 = self.Axis("Axis1")
        self.Axis2 = self.Axis("Axis2")
        self.Axis3 = self.Axis("Axis3")
        self.Axis4 = self.Axis("Axis4")
        
        # Buttons
        self.ButtonA = self.Button("ButtonA")
        self.ButtonB = self.Button("ButtonB")
        self.ButtonX = self.Button("ButtonX")
        self.ButtonY = self.Button("ButtonY")
        self.ButtonUp = self.Button("ButtonUp")
        self.ButtonDown = self.Button("ButtonDown")
        self.ButtonLeft = self.Button("ButtonLeft")
        self.ButtonRight = self.Button("ButtonRight")

'''
# Example usage
controller = Controller()

# Simulate joystick movement
controller.Axis1.set_position(50)
controller.Axis2.set_position(-75)
controller.Axis1.get_position()

# Simulate button presses and releases
controller.ButtonA.press()
controller.ButtonA.is_pressed()
controller.ButtonA.release()
controller.ButtonA.is_pressed()
'''