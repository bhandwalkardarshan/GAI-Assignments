# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverseString(str) :
    reversed=""
    for char in str[::-1] :
        reversed += char
    
    return reversed

str = "Python"
print("input string is", str, "reversed is", reverseString(str))


# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

def countVowels(str) :
    count = 0
    for char in str :
        if char == "a" or char=="e" or char=="i" or char =="o" or char=="u":
            count+=1

    return count

str = "Hello"
print("count of vowels is", countVowels(str))