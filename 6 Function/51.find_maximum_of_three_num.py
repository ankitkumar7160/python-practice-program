# Maximum Number Function
def maximum_number(number1, number2, number3):
    
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number3 and number2 > number1:
        return number2
    else:
        return number3

number1 = int(input("Enter Number First: "))
number2 = int(input("Enter Number Second: "))
number3 = int(input("Enter Number Third: "))

result = maximum_number(number1, number2, number3)

print(result)