# Methods

print(dir(dict()))

student = {"Name":"Tejeswar","Id":262}
print(student)

# dict.keys() # return list of all the keys
print(student.keys())
for i in student.keys():
    print(student[i])

# dict.values() - return all the values

print(student.values())

for i in student:
    print("{}:{}".format(i,student[i]))

# dict.items() - return all the key-value pairs

print(student.items())
for i in student.items():
    print("Key:",i[0])
    print("Value:",i[1])

keys = [1,2,3,4]
values = [1,2,3,4]
d = dict.fromkeys(keys,0)
k=0
for i in d:
    d[i] = values[k]
    k+=1
print(d)


# get()
branch = student.get("Branch")
if branch:
    print(branch)
else:
    print("Key is not available in dict")
    


#pop() - delete

print(d.pop(1))
print(d)
d.popitem()
print(d)

#setdefault()

d.setdefault(9,0)
print(d)

# update()
d2 = {"Branch":"CSE","College":"SRM"}
d.update(d2)
print(d)

# Nested Dictionary

students = {"student1":{"name":"tejasri","id":33,"marks":[98,67,45,90]},"student2":{"name":'bhavani',"id":46}}
print(students.keys())
print(students.values())












