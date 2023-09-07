import string
import random

a1=string.ascii_lowercase

a2=string.ascii_uppercase

a3=string.digits

a4=string.punctuation

password_len=int(input("Enter password Lenght\n"))
a=[]
a.extend(list(a1))
a.extend(list(a2))
a.extend(list(a3))
a.extend(list(a4))

random.shuffle(a)
print("Your Password is")
print("".join(a[0:password_len]))
