# define a Base or parent class

class AClass():
    def __init__(self):
        print("i\'m a Constructor from class A")
    def method_A(self):
        return "i\'m a method from class A"


# create a derived class or child class

class B(AClass):
    def __init__(self):
        print("i\'m a Constructor from class B (child class)")
        super().__init__()
    def method_B(self):
        return "i\'m a method from class B (child class)"
