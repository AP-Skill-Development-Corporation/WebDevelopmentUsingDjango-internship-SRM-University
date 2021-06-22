#  Encapsulation
# Getter and Setter Exmple

# whhich are used to access the data indirectly

class Employee():
    __id = 1

    def set_eid(self, eid):
        self .__id = eid

    def get_eid(self):
        return self.__id


obj = Employee()

print(obj.get_eid())

obj.set_eid(33)
print(obj.get_eid())
