from Inheritance_1 import MainClass
from multi_level_Example import GParent

class Multiple(MainClass,GParent):
    def method_Multiple(self):
        return "i'm from multiple method"
