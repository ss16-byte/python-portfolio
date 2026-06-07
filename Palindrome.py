userword = input("Enter a word to test: ").lower()
original_text = "radar"
reversed_text = userword[::-1]
test_text = "space"
flipped_text = test_text[::-1]
if userword == reversed_text:
    print("It matches! It is a palindrome.")
else:
    print("No match. It is not a palindrome.")