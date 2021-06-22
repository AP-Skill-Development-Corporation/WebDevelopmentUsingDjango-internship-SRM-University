# constructor
# it is method, which is automatically executed when we creating an object
# the function begins double underscore "__" are called as special functions, these special functions have some special meaning


class MyClassConstructor():
    def __init__(self):
        print('i\'m from Constructor')
    def Myfun(self):
        print('hi from myfun')


class Checking():
    def Myfun(self):
        print('hi from myfun')

class Apssdc():
    def __init__(self, a, b):
        self.val_a = a
        self.val_b = b

    def display(self):
        print(self.val_a, self.val_b)


a = Apssdc(1,2)
peinr(a.display())
        
