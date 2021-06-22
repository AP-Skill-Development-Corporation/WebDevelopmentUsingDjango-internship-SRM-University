# abstraction class

# the implementations are done at child class but the declarartions are
# at abstraction class

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass


class Parent(ABC):
    @abstractmethod
    def method(self):
        pass
    @abstractmethod
    def disp(self):
        pass
    
class Child(Parent):
    def method(self):
        print("apssdc")
    def disp(self):
        print('displ')
