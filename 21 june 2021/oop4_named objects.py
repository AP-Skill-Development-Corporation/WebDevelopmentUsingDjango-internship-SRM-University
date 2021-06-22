# named object
class MyClass():
    def disp(self):
        print('hello')


a =  MyClass()
print('named object :',a.disp())
print('name less object :',MyClass().disp())
