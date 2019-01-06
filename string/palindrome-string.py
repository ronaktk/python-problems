# Check if the given string is palindrome or not

def isPalindrome(str):
  str = str.replace(" ","")
  return str == str[::-1]

# Example
print(isPalindrome("wow"))
print(isPalindrome("hi"))
