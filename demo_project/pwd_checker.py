name = input("name is: ")
pwd = input("password is: ")
length = len(pwd)
new_pwd = len(pwd) * '*'


print(f"{name} you password {new_pwd} is {length} letters long")