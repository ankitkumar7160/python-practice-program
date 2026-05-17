def palind(word):
    
    word = word.lower()   # Convert word to lowercase for case-insensitive checking
    
    left = 0              # Starting index
    right = len(word)-1   # Ending index
    is_palindrome = True  # Assume word is palindrome initially

    # Compare characters from both sides
    while left < right:
        if word[left] != word[right]:
            is_palindrome = False
            break
        
        left += 1
        right -= 1

    # Print result
    if is_palindrome:
        print("Word is palindrome.")
    else:
        print("Word is not palindrome.")

word = input("Enter the word: ")
palind(word)