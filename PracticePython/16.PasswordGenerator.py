import random
import string

def passwordgenerator():
    length = int(input("How long do you want your password to be?: "))
    signs = string.ascii_letters + string.digits + string.punctuation
    i = 0
    passwordlist = []
    while i < length:
        passwordlist.append(random.choice(signs))
        i += 1
    password = ''
    for element in passwordlist:
        password += str(element)
    return password

print(passwordgenerator())