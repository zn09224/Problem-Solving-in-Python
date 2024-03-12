def binary_search_iterative(lst,item):
    
    l = 0
    h = len(lst) - 1
    found = None
    
    while l <= h:
        
        m = (l + h)//2
        
        if lst[m] == item:
            found = m
            break
        
        elif item < lst[m]:
            h = m-1
        
        elif item > lst[m]:
            l = m+1
     
    if found == None:
        found = -1
    
    return found

if __name__ == "__main__":
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42],3)) #Output should be -1
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42],17)) #Output should be 5
    