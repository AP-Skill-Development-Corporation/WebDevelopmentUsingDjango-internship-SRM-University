# Inheritance
# Inheritance is a way of defining newclass using details of existing class.
# We can call newly formed calss as derived class or child class.
# the existing class is called as base class or parent classs.

# parent class
class MainClass:
    def m1(self):
        print("Perent class")


# child classs
class SubClass(MainClass):
    def fun_subclass(self):
        print("this is from subclass function")


# create an object for both th classes
#main_obj = MainClass()
#child_obj = SubClass()

#print(main_obj.m1()) # result : Perent class
#print(child_obj.m1())
#print(child_obj.fun_subclass())
#print(main_obj.fun_subclass()) # result it will rise an error AttributeError
