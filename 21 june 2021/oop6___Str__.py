# __str__

class SpecialSrtMethod():
    def __str__(self):
        return 'you are trying to get me'
    def add(self, a, b):
        print(a+b)


class SpecialSrtMethodCheckong():
    
    def add(self, a, b):
        print(a+b)

normal = SpecialSrtMethodCheckong()
special = SpecialSrtMethod()

print(normal)
print(special)
