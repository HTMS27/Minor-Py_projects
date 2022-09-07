import random
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
ln=int(input("enter length of password:"))
print("generated password:", "".join(random.sample(a,ln)))
