import string
import random

def generator():
    s1 = string.ascii_letters
    
    s2 = string.digits

    s3 = string.punctuation

    passwordlength = int(input("Enter the Password length\n"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    random.shuffle(s)
    password = ("".join(s[0:passwordlength]))
    print(password)

generator()