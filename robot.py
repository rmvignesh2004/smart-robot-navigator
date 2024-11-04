# robot.py
class Robot:
    def __init__(self, position):
        self.position = position

    def move_to(self, position):
        self.position = position
        print(f"Robot moved to {self.position}")

    def get_position(self):
        return self.position
