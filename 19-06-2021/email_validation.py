import re


s = input("Enter your email: ")

pattern = "^[a-z][a-z0-9._]{7,15}[@](gmail.com)"


def emailValidation(s,pattern):
    if re.match(pattern,s):
        return True
    return False


print(emailValidation(s,pattern))
