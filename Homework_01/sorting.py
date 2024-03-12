import math 

# Create an array:
def initialize_matrix(n: int) -> list[list[int]]:
    new_matrix = [[None for i in range(n)] for j in range(n)]
    return new_matrix

# Returns the number of elements in an array:
def length(arr: list[int]) -> int:
    l = 0
    for i in arr:
        if i is not None:
            l += 1
    return l

# Returns the maximum value from an array:
def get_maximum(arr: list[int]) -> int:
    max = 0
    for i in range(length(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

# The insertion sorting algorithm:
def insertion_sort(arr: list[int]) -> None:
    for i in range(1, length(arr)):
        e = arr[i]
        j = i  - 1
        while j >= 0 and e < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = e

# Partition and prevail algorithm as defined in Pdf:
def partition_and_prevail(arr: list[list[int]]) -> None:
    
    max = get_maximum(arr)
    leng = length(arr)
    group_size = math.ceil((max + 1)/leng)
    new_matrix = initialize_matrix(leng)
    
    for i in range(leng):
        row_number = math.floor(arr[i]/group_size)
        for j in range(leng):
            if new_matrix[row_number][j] == None:
                new_matrix[row_number][j] = arr[i]
                break
    
    for i in range(leng):
            insertion_sort(new_matrix[i])
    
    count = 0
    for i in range(leng):
        for j in range(leng):
            if new_matrix[i][j] != None:
                arr[count] = new_matrix[i][j]
                count += 1
            else:
                break       

# Main function to read input text file and return final output:
def main(filename) -> list[list[int]]:
    with open(filename, 'r') as file:
        array_str = file.read().strip()
        array_str = array_str[1:-1]
        arr = [x for x in array_str.split(', ')]
         
    for i in range(length(arr)):
        if arr[i] == "None":
            arr[i] = None
        else:
            arr[i] = int(arr[i])
    
    if length(arr) > 0:        
        partition_and_prevail(arr)
        return arr
    else:
        return arr

main("Inputs/sorting01.txt")
main("Inputs/sorting02.txt")
main("Inputs/sorting03.txt")
