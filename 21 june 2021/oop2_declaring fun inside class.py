# declaring a Functions in side the Calss
# to represent this function is belongs to the class
# - we need to mention self as mendetory perametor.

class Myclass:
    def my_fun(self):
        print("hi")
    def say_hi(self, name):
        print("hi "+ name)



# Declaring the variable inside the class
# to represent class variable always use selfkeyword
class Myclass2:
    a = 12 # attributes
    b = 10
    def my_fun(self):
        print(self.a + self.b)
    def checking(self):
        print(a,b)# NameError: name 'a' is not defind
        
