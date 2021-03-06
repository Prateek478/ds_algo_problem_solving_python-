"""
Longest Palindromic Substring
Given a string, find the longest substring which is palindrome.
For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.
"""

# This problem solves using dynamix programmin bottom up approach, setup [i][i] as true and then check 2 length string and then 
#new loop to keep on increasing the length of the string until the end and based on start and maxlength value return the output.

def longestPalSubstr(st) :
	n = len(st) # get length of input string

	# table[i][j] will be false if substring str[i..j] is not palindrome. Else table[i][j] will be true
	table = [[0 for x in range(n)] for y
					 in range(n)]

	# All substrings of length 1 are palindromes
	maxLength = 1
	i = 0
	while (i < n) :
		table[i][i] = True
		i = i + 1

	# check for sub-string of length 2.
	start = 0
	i = 0
	while i < n - 1 :
		if (st[i] == st[i + 1]) :
			table[i][i + 1] = True
			start = i
			maxLength = 2
		i = i + 1

	# Check for lengths greater than 2.k is length of substring
	k = 3
	while k <= n :
		# Fix the starting index
		i = 0
		while i < (n - k + 1) :

			# Get the ending index of substring from starting index i and length k
			j = i + k - 1

			# checking for sub-string from ith index to jth index iff st[i+1] to st[(j-1)] is a palindrome
			if (table[i + 1][j - 1] and
							st[i] == st[j]) :
				table[i][j] = True

				if (k > maxLength) :
					start = i
					maxLength = k
			i = i + 1
		k = k + 1
	print "Longest palindrome substring is: " ,st[start:start + maxLength]

	return maxLength # return length of LPS


if __name__ == "__main__":
	print longestPalSubstr("forgeeksskeegfor")
