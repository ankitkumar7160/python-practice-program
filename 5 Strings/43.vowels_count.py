def count_consonent(word):
    count = 0
    vowel = "aeiouAEIOU"
    
    for i in word:
        if i .isalpha():
            if i not in vowel:
                count += 1
    return count

word = input("Enter the string: ").lower()
result = count_consonent(word)
print(result)