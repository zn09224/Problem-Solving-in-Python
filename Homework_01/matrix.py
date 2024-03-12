# Creates an array:
def init_matrix(rows: int, cols: int) -> list[list[int]]:
    return [[None for _ in range(cols)] for _ in range(rows)]


def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    rows = len(image)                       # Number of rows in image matrix
    cols = len(image[0])                    #Number of columns in image matrix
    width = kernel[0]                       #Width of the kernel
    convo_matrix = init_matrix(rows, cols)  #Creating the converted matrix array
    
    for i in range(rows):
        for j in range(cols):
            
            sum = 0     # To sum up the pixel converted values
            count = 0   # Varaible used later to map kernel values
            
            # Loops to check the the overlapping values of kernel and image pixels
            for l in range(i - (width//2), i + (width//2) + 1):
                
                if (l < 0 or l >= rows):
                    count += width
                    continue
                
                for s in range(j - (width//2), j + (width//2) + 1):
                                   
                    if (s < 0 or s >= cols):
                        count += 1
                        continue
                    
                    else:
                        kernel_value =  ((width*count) + 1) % (width * width - 1)   # Mapping of 1d kernel to n x n kernel
                        sum = sum + image[l][s] * kernel[kernel_value]
                        count += 1
                
            if j != cols - 1:             
                convo_matrix[i][j] = sum - image[i][j]
            else:
                convo_matrix[i][j] = sum
    
    return convo_matrix
                        

# Main function to take input from given text file(s) and return the final output:
def main(file_name: str) -> list[list[int]]:
    with open(file_name) as f :
        lines = f.readlines()
    input = []
    for line in lines :
        line = line.strip() # remove leading and trailing spaces
        tokens = line.split() # split the line into tokens
        input.append(tokens) # add the first token to the input list
        
    rows = int(input[0][0])
    cols = int(input[0][1]) 
    image = [[None for i in range(cols)] for k in range(rows)]
    
    n = 1
    for i in range(rows):
        for j in range(cols):
            image[i][j] = int(input[n][j])
        n += 1
    
    w = int(input[len(input) - 1][0])
    kernel = [None for i in range((w*w) + 1)]
    for i in range((w*w)+1):
        kernel[i] = int(input[len(input) - 1][i])
        
    return filter_image(image, kernel)

print(main("Inputs/matrix01.txt"))
    
