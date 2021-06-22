# multi Level inheritance

class GParent():
    def methodG(self):
        return "from GParent Method"


class Parent(GParent):
    def methodP(self):
        return "from Parent Method"

class Child(Parent):
    def methodChild(self):
        return "from child Method"


# create instance for child

c = Child()
#print(c.methodChild())# "from child Method"
#print(c.methodP())# "from Parent Method"
#print(c.methodG()) # from GParent Method
