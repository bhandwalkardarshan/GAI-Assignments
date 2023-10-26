# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

my_list = []
for i in range(1, 11):
    my_list.append(i)

my_list.append(20)
print(my_list)
my_list.remove(20)
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

sum_of_ele_list = sum(my_list)
avg_of_ele_list = sum_of_ele_list / len(my_list)
print("sum of list", sum_of_ele_list, "average of list", avg_of_ele_list)