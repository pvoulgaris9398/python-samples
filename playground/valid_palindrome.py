# Define ANSI codes
GREEN = "\033[32m"
RED = "\033[1;31m"
RESET = "\033[0m"  # Crucial: Resets color back to default

def is_valid_palindrome(s:str) -> bool:
	left = 0
	right = len(s) - 1
	
	# TODO: Check for strings that contain no valid characters and return False
	if not any(char.isalpha() for char in s):
		return False

	while (left < right):

		# If current left character is not alphabetic move to the right
		while (not s[left].isalpha() and left < right):
			left += 1
		
		# If current right character is not alphabetic move to the left
		while (not s[right].isalpha() and right > left):
			right -=1
	
		# Check in case-insensitive manner, return if not the same
		# (we found a diff that would break the rule)
		if s[left].lower() != s[right].lower():
			return False
			
		left += 1
		right -= 1

		
	return True

def test1():
	test = "A man, a plan, a canal panama!"
	result = is_valid_palindrome(test)
	color = GREEN if result else RED
	print(f"{color}'{test}' {'is' if result else' is NOT'} a valid palindrome!{RESET}")

def test2():	
	test = "a"
	result = is_valid_palindrome(test)
	color = GREEN if result else RED
	print(f"{color}'{test}' {'is' if result else' is NOT'} a valid palindrome!{RESET}")

def test3():
	test = "&&&"
	result = is_valid_palindrome(test)
	color = GREEN if result else RED
	print(f"{color}'{test}' {'is' if result else 'is NOT'} a valid palindrome!{RESET}")

if __name__ == "__main__":
	
	test1()
	test2()
	test3()