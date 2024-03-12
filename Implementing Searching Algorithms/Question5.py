def finding_multiple(lst, item):
    
    output = []
    
    l = 0
    h = len(lst) - 1
    
    
    while l <= h:
        
        m = (l + h)//2
        
        if lst[m] == item:
            break
        
        elif item < lst[m]:
            h = m-1
        
        elif item > lst[m]:
            l = m+1
    
    for i in range(m, -1, -1):
        if lst[i] == item:
            output.insert(0, i)
        else:
            break
                
    for j in range(m + 1, len(lst)):
        if lst[j] == item:
            output.append(j)
        else:
            break  
        
    return output

if __name__ == "__main__":
    print(finding_multiple([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 17)) # Output should be [5, 6, 7, 8]
    print(finding_multiple([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 34)) # Output should be []