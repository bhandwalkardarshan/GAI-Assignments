# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```

# ## Solution
def print_pattern(n):
    for i in range(1, n+1):
        op=""
        for j in range(1,i+1):
            op+=str(j)+" "
        print(op)

print_pattern(5)


# ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:

# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# **Expected output:**

# ```
# 75
# 150
# 145
# ```
def func(arr):
    for num in arr:
        if num > 500:
            break
        if num % 5 == 0 and num <= 150 :
            print(num)  
numbers = [12, 75, 150, 180, 145, 525, 50]
func(numbers)



# ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:

# ```
# AuKellylt
# ```

s1 = "Ault"
s2 = "Kelly"
print("".join([s1[:len(s1)-2], s2, s1[-1]]))

# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:

# ```
# yaivePNT
# ```
def lowerFirst(str):
    lower=""
    upper=""
    for char in str:
        if char.islower():
            lower += char
        else:
            upper += char
    
    return lower+upper
str1 = "PyNaTive"
print(lowerFirst(str1))
# ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**

# ```
# ['My', 'name', 'is', 'Kelly']
# ```

def mergeL1L2(l1,l2):
    mergedList=[]
    l1_index=0
    l2_index=0
    while (l1_index<len(l1) and l2_index<len(l2)):
        mergedList.append(l1[l1_index]+l2[l2_index])
        l1_index+=1
        l2_index+=1
    return mergedList

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(mergeL1L2(list1,list2))
# ### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**

# ```
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ```

def concatTwoListsInOrder(l1,l2):
    result=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            result.append(l1[-i]+l2[-j])
    print(result)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatTwoListsInOrder(list1,list2)

# ### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**

# ```
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# ```

# **Expected output:**

# ```
# 10 400
# 20 300
# 30 200
# 40 100
# ```

def iterate(l1,l2):
    j=len(l2)
    for i in range(len(l1)):
        j = len(l2) - 1 - i 
        print(l1[i],l2[j])
    

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate(list1,list2)

# ### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**

# ```
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
# ```
def init_dict(employees,defaults):
    employee_dict = {}
    for emp in employees:
        employee_dict[emp] = {k: v for k,v in defaults.items()}
    return employee_dict
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
print(init_dict(employees,defaults))

# ### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

# ```
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# ```

# **Expected output:**

# ```
# {'name': 'Kelly', 'salary': 8000}
# ```
# ## Solution
def extract_keys(sample_dict, keys):
    extracted_dict = {key: sample_dict[key] for key in keys if key in sample_dict}
    return extracted_dict
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
print(extract_keys(sample_dict, keys))

# ### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**

# ```
# tuple1: (11, [222, 33], 44, 55)
# ```
# ## Solution
tuple1 = (11, [22, 33], 44, 55)
new_element = 222
index = 1
tuple1 = list(tuple1)
tuple1[index][0] = new_element
tuple1 = tuple(tuple1)
print("tuple1:", tuple1)
