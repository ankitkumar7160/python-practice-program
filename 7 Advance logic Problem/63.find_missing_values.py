# def missing_values(my_array,n):
    
#     excepted_sum = (n*(n+1))/2
#     actual_sum = 0
    
#     for num in my_array:
#         actual_sum += num

#     missing_values = excepted_sum - actual_sum
#     return missing_values

# my_array = input("Enter Values of array: ")
# new_array = [int(x) for x in my_array.split()]
# n = len(new_array)+1

# result = missing_values(new_array, n)
# print(result)



#find missing value for 1 to 9 withut any pattern
def missing_values(my_array):
    
    min_val = min(my_array)
    max_val = max(my_array)
    n_list = []
    
    for i in range(min_val,max_val+1):
        if i not in my_array:
            n_list.append(i)
    return n_list
        
my_array= [1,3,6,9]

print(missing_values(my_array))