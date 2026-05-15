def calculate_GCD(a, b):
    while b != 0:
        remainder = a % b  
        a = b              
        b = remainder      
    return a

def array_gdc(my_array):
    
    current = my_array[0]
    
    
    for num in range(1, len(my_array)):
        next_val = my_array[num] 
        
        current = calculate_GCD(next_val, current)
        
    return current

my_array = input("Enter the array (space separated): ")


new_array = [int(x) for x in my_array.split()]

result = array_gdc(new_array)

print(f"The GCD of the entire array is: {result}")