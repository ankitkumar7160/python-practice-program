def convert_to_upper(sentence):
    result = ""
    
    for char in sentence:
        code = ord(char)
        
        if code >= 97 and code <= 122:
            upper_code = code - 32
            upper_char = chr(upper_code)
            result += upper_char

        else:
            result += char
    return result

sentence = input("Enter the sentence: ")
result = convert_to_upper(sentence)

print(f"Original Sentence ({sentence})")
print(f"Uppercase Sentence ({result})")