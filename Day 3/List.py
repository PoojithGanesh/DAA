def process_list(lst):
    if not lst:  
        return lst
    return sorted(lst)  
# Test Cases
print(process_list([]))             
print(process_list([1]))             
print(process_list([7, 7, 7, 7]))     
print(process_list([-5, -1, -3, -2, -4]))  
