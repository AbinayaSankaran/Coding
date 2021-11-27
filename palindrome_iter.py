# check whether the string is palindrome or not
"""
A palindrome is a word, sentence, verse, or even number that reads the same backward or forward. 
"""
# Iterative method
def isPalindrome(s):

	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] != s[j]:
			return False
		i = i + 1
		j = j - 1

	return True


if __name__ == '__main__':

	s = input("Enter the string: ")

	if isPalindrome(s):
		print('Palindrome')
	else:
		print('Not Palindrome')
