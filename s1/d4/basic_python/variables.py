# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

num = 10
print(f"Type of {num}: {type(num)}, value: {num}...")

pi = 3.142
print(f"Type of {pi}: {type(pi)}, value: {pi}...")

isRight = True
print(f"Type of {isRight}: {type(isRight)}, value: {isRight}...")

my_list = [1, 2, 3, 'apple', 'banana']
print(f"Type of {my_list}: {type(my_list)}, length: {len(my_list)}...")
for item in my_list :
    print(item)

# tuples are immutable
tuple = ['x', 'y', 'z', 'a', 'b']
for item in tuple :
    print(item)

my_set = {1,2,3,4,5}
for item in my_set :
    print(item)

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
for key,value in my_dict.items() :
    print(f"Key: {key}, Value : {value}")
