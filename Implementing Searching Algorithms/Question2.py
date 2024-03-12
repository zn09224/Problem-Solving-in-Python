def binary_search_iterative_modified(lst,item):
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
        
        if l > h:
            lst.insert(l, item)
            return l    
    
    return found

if __name__ == "__main__":
    print(binary_search_iterative_modified([0, 1, 2, 8, 13, 17, 19, 32, 42], 8)) # Output should be 3
    print(binary_search_iterative_modified([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], -1)) # Output should be 0
    