# Remove Duplicate Element
def remove_duplicate_element(my_array):
    
    uniqe_set = {}
    
    duplicate_list = []
    
    for num in my_array:
        
        if num not in uniqe_set:
            duplicate_list.append(num)

            uniqe_set[num] = True
        
    return duplicate_list

my_input = input("Enter array values: ")

new_array = [int(x) for x in my_input.split()]

result = remove_duplicate_element(new_array)
print(f"List after removing duplicates: {result}")