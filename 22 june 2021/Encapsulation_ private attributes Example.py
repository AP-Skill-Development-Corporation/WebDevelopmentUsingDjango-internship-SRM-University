# Encapsulation:
# the process of binding the data.(hiding the impleentations)
# for binding the data we need to use the private modifiers (__name)

# private attribute
class A:
    __a = 10

    def disp(self):
        print(self.__a)

a = A()
a.disp()

print(a.__a) # AttributeError:
