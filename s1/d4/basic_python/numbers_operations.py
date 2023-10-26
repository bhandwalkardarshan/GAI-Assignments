# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."
def is_prime(number):
    if number <= 1:
        return False  

    if number <= 3:
        return True  

    if number % 2 == 0 or number % 3 == 0:
        return False  

    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

number = 13
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def fact(n) :
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n=5
print("factorial of",n, "is", fact(n)) 

# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci(num):
    seq = [0, 1]
    while len(seq) < num:
        seq.append(seq[-1] + seq[-2])
        
    return seq[:num]

n=5
print("fibonacci sequence is ",fibonacci(n))

# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

squares = [x**2 for x in range(1,11)]
print(squares)