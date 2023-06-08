# What is functional programming?
#  functions operate on well-defined data structures. Clean and understandable. memory efficient.
# Pure functions - separation between data and behaviour

def multi_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multi_by_2([1, 2, 3]))

# 1st rule - no matter how many times we pass on the inputs , the results should be the same every time.
# 2nd rule - produces no side effects. less buggy code, easy to understand code
