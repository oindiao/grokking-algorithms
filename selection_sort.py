def find_smallest(arr):
    
    smallest = arr[0]
    smallest_index = 0
    
    for index in range(1, len(arr)) :
        
        if arr[index] < smallest :
            
            smallest = arr[index]
            smallest_index = index
    
    return smallest_index

def selection_sort(arr):

    new_arr = []
    
    for index in range(len(arr)) :
        
        smallest = find_smallest(arr)
        new_arr.append(arr[smallest])
        arr.pop(smallest)

    return new_arr

print(selection_sort([3,6,2,5]))