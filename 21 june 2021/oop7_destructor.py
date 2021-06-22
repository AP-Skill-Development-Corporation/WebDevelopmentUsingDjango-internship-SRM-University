# __del__
# destructor, will be called when you delete an object

class ClassDel():
    pass

class SpecialClassDel:
    def __del__(self):
        print("your object is distroyed")

