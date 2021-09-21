import random;

lower = "acdefghijklmopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}*;/,-"

all = lower + upper + number + symbols

length = 25
password = "".join(random.sample(all,length))
print(password)
input()