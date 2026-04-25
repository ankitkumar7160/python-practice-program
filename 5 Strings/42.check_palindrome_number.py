def palind(word):
    
    word = word.lower()
    
    left = 0
    right = len(word)-1
    is_palindrome = True

    while left<right:
        if word[left] != word[right]:
            is_palindrome = False
            break
        
        left +=1
        right -=1

    if is_palindrome :
        print("Word is palindrome.")
    else:
        print("Word is not palindrome.")

word = input("Enter the word: ")
palind(word)