import string
import random

char = string.ascii_letters + string.digits + string.punctuation
number = int(input("choose the length of your password"))

def password(length):

    result = ''.join(random.choice(char) for i in range(length))
    print(result)


password(number)
