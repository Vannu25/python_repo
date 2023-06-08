
val = "2023-02-26 22:58:18.597000-08:00"   # sf time
val2 = "2023-02-27 12:13:50.186701"   # curr time


str1 = val.split('.')
print(str1[0])

str2 = val2.split('.')
print(str2[0])

if str1 > str2:   # created time is not greater than current time.
    print("error , time is greater than current time")
else:
    print("success")
