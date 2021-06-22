# Polymorphism
# one Functional with miltiple behaviour

# over riding an attribute 
class Parent():
    name = 'Lakshman'

class child(Parent):
    # name = 'Lucky'
    phone = '123'


# over riding methods

class Parent1():
    def career(self):
        return 'Engineer'

class child1(Parent):
    def career(self):
        return "Photographer"
    
