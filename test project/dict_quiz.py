student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

m = student.get('marks')
print(m)

dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age") - key error
# print(temp)


student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

student.pop("marks")
# print(student)

# del student["marks"]
# student.popitem()  # last item


# student.remove("marks")  # remove object is not available.
print(student)
