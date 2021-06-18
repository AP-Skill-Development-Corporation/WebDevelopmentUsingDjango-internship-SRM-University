# generators

def generator_object():
    yield 1
    yield 2
    yield 3
    yield 4
    
def sample():
    yield 'apssdc'
    yield 'SRM'
    yield 'Students'
    yield 1
    yield [1,3,4]

# tuple comprehension
result = tuple(i for i in range(10))
print(result)
print(type(result))

tuple_generator = (i for i in range(10))
print(tuple_generator)
print(type(tuple_generator))
