def palindrome(str_check):
    left = 0
    right = len(str_check) - 1
    while left < right:
        if str_check[left] != str_check[right]:
            return False
        left = left + 1
        right = right - 1   
    return True


s = input("Enter a string: ")
if palindrome(s):
    print(s, "is Palindrome")
else:
    print(s, "is not Palindrome")
