def binary_search_recursive_modified(lst, item, l, h):
    
    m = (l +h) // 2 
    
    if l > h:
        lst.insert(l, item)
        return l
        
    if lst[m] == item:
        return m
        
    elif item < lst[m]:
        return binary_search_recursive_modified(lst, item, l, m - 1)
            
        
    elif item > lst[m]:
        return binary_search_recursive_modified(lst, item, m+1, h)

if __name__ == "__main__":
    print(binary_search_recursive_modified([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, 0, 8)) # Output should be 3
    print(binary_search_recursive_modified([0, 1, 2, 8, 13, 17, 19, 32, 42], 17, 0, 8)) # Output should be 5