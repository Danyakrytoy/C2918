class Hello:
    def __init__(self):
        print("Hello")

class HelloWorld(Hello):

    def __init__(self):
        super().__init__()
        print("World!")

hello_world = HelloWorld()


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"

class Laptop:
    def __init__(self):
        super().__init__()
        self.processor = "Intel Core i9‑12900HK (Alder Lake‑P)"

class Size_screen:
    def __init__(self):
        super().__init__()
        self.size = "(6.06 inches)"

class SmartPhone(Display, Computer, Laptop, Size_screen):
    def print_into(self):
        print(self.size)
        print(self.processor)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone()
iphone.print_into()