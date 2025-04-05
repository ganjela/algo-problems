"""
We compare the string to its reverse to determine if it is a palindrome.
"""
def validate_palindrome(s):
    return s == s[::-1]

