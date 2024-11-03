class Brain:
    class Screen:
        def __init__(self):
            self.content = ""  # Stores the screen content

        def print(self, text):
            """Simulate printing text to the Brain screen."""
            self.content += text + "\n"
            print(text)  # This simulates the output to the Brain screen

        def clear_screen(self):
            """Simulate clearing the Brain screen."""
            self.content = ""
            print("Screen cleared!")  # Simulate the clear screen action

        def print_at(self, x, y, text):
            """Simulate printing at specific coordinates on the Brain screen."""
            print(f"Printing at ({x}, {y}): {text}")

    class Timer:
        def __init__(self):
            import time
            self.start_time = time.time()

        def time(self, unit="seconds"):
            """Return the elapsed time in the specified unit (seconds by default)."""
            import time
            elapsed_time = time.time() - self.start_time
            if unit == "seconds":
                return elapsed_time
            elif unit == "milliseconds":
                return elapsed_time * 1000
            elif unit == "microseconds":
                return elapsed_time * 1000000

        def reset(self):
            """Reset the timer to zero."""
            import time
            self.start_time = time.time()
            print("Timer reset")

    def __init__(self):
        self.screen = self.Screen()
        self.timer = self.Timer()


class GearSetting:
    RATIO36_1 = "36:1"
    RATIO18_1 = "18:1"
    RATIO6_1 = "6:1"    
    RATIO_36_1 = "36:1"
    RATIO_18_1 = "18:1"
    RATIO_6_1 = "6:1"


class Ports:
    # Define the available ports as class attributes
    PORT1 = "PORT1"
    PORT2 = "PORT2"
    PORT3 = "PORT3"
    PORT4 = "PORT4"
    PORT5 = "PORT5"
    PORT6 = "PORT6"
    PORT7 = "PORT7"
    PORT8 = "PORT8"
    PORT9 = "PORT9"
    PORT10 = "PORT10"
    PORT11 = "PORT11"
    # Add more ports if needed

class Motor:
    def __init__(self, port):
        self.port = port
        self.velocity = 0  # Motor velocity in percentage (0-100)
        self.direction = 1  # 1 for forward, -1 for reverse
        self.position = 0  # Motor position in degrees
        print(f"Motor initialized on {self.port}")

    def get_velocity(self):
        """Return the motor's current velocity."""
        print(f"Motor on {self.port} velocity: {self.velocity}%")
        return self.velocity


    def set_velocity(self, velocity, unit="percent"):
        """Set the motor's velocity."""
        if unit == "percent":
            self.velocity = velocity
        print(f"Motor on {self.port} set to {velocity}% velocity")

    def spin(self, direction="forward"):
        """Spin the motor in a specified direction."""
        if direction == "forward":
            self.direction = 1
        elif direction == "reverse":
            self.direction = -1
        print(f"Motor on {self.port} spinning {direction}")

    def stop(self):
        """Stop the motor."""
        self.velocity = 0
        print(f"Motor on {self.port} stopped")

    def reset_position(self):
        """Reset the motor's position to zero."""
        self.position = 0
        print(f"Motor on {self.port} position reset")

    def get_position(self):
        """Return the motor's current position."""
        print(f"Motor on {self.port} position: {self.position}")
        return self.position

    def set_position(self, position):
        """Set the motor's position to a specific value."""
        self.position = position
        print(f"Motor on {self.port} position set to {self.position}")

    def set_brake(self, mode="coast"):
        """Set the motor's braking mode."""
        print(f"Motor on {self.port} brake mode set to {mode}")



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
