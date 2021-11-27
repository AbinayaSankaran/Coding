def isPalindrome(s, low, high):
 
    # base case
    if low >= high:
        return True
 
    # return false if mismatch happens
    if s[low] != s[high]:
        return False
 
    # move to the next pair
    return isPalindrome(s, low + 1, high - 1)
 
 
if __name__ == '__main__':
 
    s = input("Enter the string: ")
    if isPalindrome(s, 0, len(s) - 1):
        print('Palindrome')
    else:
        print('Not Palindrome')

        