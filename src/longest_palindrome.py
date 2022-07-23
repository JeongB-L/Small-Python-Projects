#	the two pointer moves from the middle of the string, and it keeps expanding untill it is not a palindrome,
#	or it reaches the end, then it returns the index for the current palidrome-certified locations. 
def expand(left, right):
	while left >= 0 and right < len(s) and s[left] == s[right]:
		left -= 1
		right += 1
		#	adding 1 to the left side index is necessary as the function automatically subtracts 1 from the final result
		#	now the longest palindrome from the given index is returned
	return s[left + 1: right]
def longest_palindrome(s):
	#	filters the case where the given is already a palindrome by itself
	result = ''
	if len(s) < 2 or s == s[::-1]:
		return s
	for i in range(0, len(s) - 1):
		#	continuously expanding; checkes the palindrome for each odd and even idices
		#	key is length of the string
		result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
	return result
		
		
	
if __name__ == "__main__":
	s = '123454321'