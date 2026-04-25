# text = input("Enter string: ")
# reverse = ""

# for i in text:
#     reverse = i + reverse
    
# print(reverse)

def reverse_string(text):
    reverse = ""
    
    for i in text:
        reverse = i + reverse
        
    return reverse


word = input("Enter string: ")
print(reverse_string(word))