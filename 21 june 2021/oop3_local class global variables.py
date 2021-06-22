# local variable, class and global variable

i , j = 10,20 # global variables
a, b = 204, 306 # global variables

class Variable():
    a, b = 2, 4 # class Variables
    def add(self, x,y): # loacl Variables
        print(x,y)
        print(self.a, self.b)
        print(i,j)


# local variable, class and global variable with same names

class VariableWithSameNames():
    a, b = 88, 99 # class variable
    def check(self,a,b):
        print(a,b) # local
        print(self.a,self.b) # class 
        print(globals()['a'],globals()['b']) # global
