def get_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b 
        b = remainder
    return a

def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    
    return (a * b) / get_gcd(a, b)

def find_array_lcm(my_array):
    result = my_array[0]
    
    for num in range(1, len(my_array)):
        current_number = my_array[num]
        
        result = get_lcm(result, current_number)
    return result

my_array = input("Enter the array (space separated): ")

new_array = [int(x) for x in my_array.split()]

Result_lcm = find_array_lcm(new_array)
print(f"LCM of the array is: {Result_lcm}")