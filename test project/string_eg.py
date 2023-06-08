original_string = input("The original string is : ")
size = len(original_string)
# for i in range(0, size-1, 2):
#      print(original_string[i])

x = list(original_string)
for i in x[0::2]:
    print(i)