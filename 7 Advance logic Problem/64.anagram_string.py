print("Anagram Checker")
string1 = input("Enter First String: ").lower()
string2 = input("Enter Second String: ").lower()

# remove space
string1 = string1.replace(" ", "")
string2 = string2.replace(" ", "")

# check length
if len(string1) != len(string2):
    print("Not Anagram")

else:
    if sorted(string1) == sorted(string2):
        print("Anagram")
    else:
        print("Not Anagram")