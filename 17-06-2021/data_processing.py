# Write a function to count the number of lines in a given file

f = open("file1.txt","r")

data = f.read()
lines = data.split("\n")
no_of_lines = len(lines)

print(no_of_lines)


def line_count(filename):
    f = open(filename,"r")
    lines = f.readlines()
    return len(lines)

filename = "file1.txt"

result = line_count(filename)
print(result)
