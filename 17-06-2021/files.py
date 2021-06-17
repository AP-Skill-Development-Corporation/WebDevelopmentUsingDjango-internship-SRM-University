# Files

# open(filename, mode)

# create
# open("file1.txt",'x')

# write() - write data into the given file(if the file is already exist)
# if the file is not there in the location, then write() will create a new file
f = open("file2.txt","w")
f.write("Python Programming\n")
f.write("SRM University")
f.close()

# read() - to read the data in a file
f = open("file1.txt","r")
data1 = f.read(10)
print(f.tell())
f.seek(2)
print(f.tell())
data2 = f.read()
print(f.tell())
print("Data1:",data1)
print("Data2:",data2)
f.close()

# readlines()
f = open("file1.txt","r")
lines = f.readlines()
print(lines)
f.close()

# append
f = open("file1.txt","a")
f.write("This is the new data")
f.close()



















