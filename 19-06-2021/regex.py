import re

# re.match(pattern, string)

s = "Web Development with Python Web Python"

pattern = "Python"

m = re.match(pattern,s)

ser = re.search(pattern, s)

f = re.findall(pattern,s)

sp = re.split("e",s)

sub = re.sub("e","@",s,2)

print(sub)
