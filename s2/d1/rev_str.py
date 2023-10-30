def reverseString(s):
    reversed=""
    for char in s:
        reversed = char + reversed
    print(reversed)

reverseString("Python is fun")