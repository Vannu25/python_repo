import pytest

# temp = []
#
# with open('node_details.txt') as infile:
#     for column in infile:
#         if column.__contains__("Windows Server"):
#             if column.split()[0] != "NAME":
#                 temp.append(column.split()[0])
#         # print(column.split()[0])


result = []
try:
    with open('node_details.txt') as infile:
        for line in infile:
            try:
                if line.__contains__("Windows Server"):
                    name, ip, os = line.split()[0], line.split()[6], line.split()[7]
                    entry = {"Name": name, "EXTERNAL-IP": ip, "OS-IMAGE": os}
                    result.append(entry)
                    print("The data in result is : {}".format(result))
                    # return result
            except Exception as e:
               print(e)
except Exception as e:
    print(e)
    pytest.fail("The Nodes is not found for the tags:hostname")
