# # Palindrome using integer
# def palindrome(number):
#     temp = number
#     reversed_num = 0
    
#     while temp > 0:
#         digit = temp % 10
        
#         reversed_num = (reversed_num * 10) + digit
#         temp //= 10
        
#     return number == reversed_num


# number = int(input("Enter the number: "))

# if palindrome(number):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Palindrome using String    
def palindrome(text):
    reversed_text = text[::-1]
    
    return text == reversed_text


string = input("Enter the string: ")

if palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")