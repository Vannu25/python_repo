# File I/O - input and output - used to read & wrirte files.


my_file = open('test.txt')
print(my_file.read())
my_file.close()

# file mode - r - read, w - write, a - append
try:
    with open('happy.txt', mode='r+') as my_file:
        text = my_file.read()
        print(text)

except FileExistsError as err:
    print("file not found error")
    raise err

f = open("test.txt", "r")
print(f.readline(3))
f.close()
