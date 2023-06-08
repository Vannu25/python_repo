# # Open the text file and read the contents
# with open('node_details.txt', 'r') as file:
#     contents = file.read()
#
# # Split the contents into lines
# lines = contents.split('\n')
#
# # Initialize an empty dictionary
# my_dict = {"Name": "", "EXTERNAL-IP": "", "OS-IMAGE": ""}

import pandas as pd
import numpy as numpy
import csv as csv

data = pd.read_csv("node_result.csv",sep=';',engine='python',encoding='utf-8-sig')
headers = pd.read_csv("node_result.csv", index_col=0, nrows=0).columns.tolist()
columns = ['NAME']



#
# # Loop through the lines and split each line into key-value pairs
# for line in lines:
#     if line.strip() == '':
#         continue
#     key, value = line.split(':')
#     my_dict[key.strip()] = value.strip()
#
# result = []
# with open("node_details.txt") as f:
#     for line in f:
#         # (key, val) = line.split()
#         # d[int(key)] = val
#         if line.__contains__('Windows'):
#             result.append(line)
#
# print(result)



# for i in result:
#     if i.__contains__("ip"):
#         print("name exist")
#     else:
#         print("Not Exist")
# res_dct = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
# print(type(res_dct))
# print(res_dct)

