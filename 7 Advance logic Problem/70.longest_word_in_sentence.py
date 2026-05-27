def longest_word_in_sentence(sentence):
    
    new_sentence = list(sentence.split())
    
    longest_word = ""
    
    for word in new_sentence:
        
        if len(word) > len(longest_word):
            longest_word = word
        
    return longest_word

sentence = input("Enter sentence: ")

result = longest_word_in_sentence(sentence)
print(f"The longest word is: {result}")