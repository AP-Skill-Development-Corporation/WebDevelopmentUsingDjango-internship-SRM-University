from Inheritance_1 import MainClass

class A(MainClass):
    def method_A(self):
        return "from sub class A"



obj = A()
print(obj.method_A())

print(obj.m1())
