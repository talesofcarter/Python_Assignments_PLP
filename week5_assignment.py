# 1. Creating a class and adding attributes and methods to the class

class Smartphone:
    def __init__(self, brand, model, network_coverage, camera,):
        self.brand = brand
        self.model = model
        self.network_coverage = network_coverage
        self.camera = camera
        
# Methods
    def take_picture(self, photo):
        if self.camera == "48MP":
            print(f"Taking {photo} with my {self.brand} {self.model}")
        else: 
            print(f"Pixels too low for a HD picture.")

    def make_call(self, contact):
        if self.network_coverage == "5G":
            print(f"Calling {contact} with my {self.brand} {self.model}")
        else:
            print(f"Network coverage is too long to make a call")

# Inheritance or Polymorphism

class Android(Smartphone):
    def take_picture(self, photo):
        print(f"An android phone taking cinematic {photo}")

class IOSphone(Smartphone):
    def make_call(self, contact):
        print(f"Calling {contact} with {self.brand} {self.model} is awesome!")

    
smartphone1 = Smartphone("iPhone", "16 Pro Max", "5G", "48MP")
smartphone2 = Smartphone("Samsung", "S25 Ultra", "5G", "200MP")
smartphone3 = Smartphone("Google", "Pixel 10 Pro", "4G", "50MP")

# Test
print(smartphone1.take_picture('a selfie'))
print(smartphone2.take_picture('a selfie'))
print(smartphone3.take_picture('a selfie'))
print(smartphone2.make_call("my girlfriend"))
print(smartphone3.make_call("my girlfriend"))

# 2. Activity 2

class Dog:
    def move(self):
        print('Running')

class Eagle:
    def move(self):
        print("Flying")

class Snail:
    def move(self):
        print("Crawling")

