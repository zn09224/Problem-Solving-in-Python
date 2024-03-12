def binary_search_recursive(lst, item, l, h):
    
    m = (l +h)//2
    
    if l > h:
        return -1
    
    if lst[m] == item:
        return m
        
    elif item < lst[m]:
        return binary_search_recursive(lst, item, l, m - 1)
            
        
    elif item > lst[m]:
        return binary_search_recursive(lst, item, m+1, h)

if __name__ == "__main__":
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, 0, 8)) # Output should be -1
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 19, 0, 8)) # Output should be 6