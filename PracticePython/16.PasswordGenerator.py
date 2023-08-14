import random
import string

signs = string.ascii_letters + string.digits + string.punctuation
loop = random.randint(10, 20)
i = 0
passwordlist = []
while i < loop:
    passwordlist.append(random.choice(signs))
    i += 1
password = ''
for element in passwordlist:
    password += str(element)
print(password)