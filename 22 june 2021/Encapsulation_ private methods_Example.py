# Encapsulation
# creating private methods

class MyClass():
    def __disp(self):
        print('it is a private method')

    def normal_method(self):
        print('it is from normal_method')
        self.__disp()
