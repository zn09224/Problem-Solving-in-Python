# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    
    return {
        'data': [None] * size,  # list of elements
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# DO NOT CHANGE THIS FUNCTION
# Create a priority queue
def create_priority_queue(size: int) -> dict:
    
    return {
        'data': [(None, float('inf'))] * size,  # list of elements with default priority set to infinity
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    if queue['n'] == queue['size']:
        return True
    else:
        return False

# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    if queue['n'] == 0:
        return True
    else:
        return False
    
# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    
    if is_full(queue):
        return "Queue is full. Enqueue failed."
    
    else:
        queue['rear'] = (queue['rear'] + 1) % queue['size']     # Incrementing rear
        rear = queue['rear']
        
        if is_empty(queue):
            queue['front'] = rear                               # If queue is empty, point front and rear to the same location
            
        queue['n'] += 1                                         # Increasing the number of elements variable
        queue['data'][rear] = item                            

# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    if is_empty(queue):
        return "Queue is empty. Dequeue failed."
    
    else:
        front = queue['front']
        item = queue['data'][front]
        queue['data'][front] = None
        queue['n'] -= 1                                     # Decrementing the number of elements variable

        if is_empty(queue):
            queue['front'] = queue['rear'] = -1             # If queue is empty, point front and rear to the same location
            
        else:
            queue['front'] = (front + 1) % queue['size']    # Incrementing the front variable, pointing it to the second item in queue
            
        return item
        
# Return the element at the front of the queue without removing it
def peek(queue: dict):
    if is_empty(queue):
        return "Queue is empty. Peek failed."
    else:
        return queue['data'][queue['front']]
    
# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    
    if is_full(priority_queue):
        return "Priority queue is full. Enqueue failed."
    
    else:
        priority_queue['rear'] = (priority_queue['rear'] + 1) % priority_queue['size']
        rear = priority_queue['rear']
        
        if is_empty(priority_queue):
            priority_queue['front'] = rear
        
        priority_queue['n'] += 1
        priority_queue['data'][rear] = (item, priority)


# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    if is_empty(priority_queue):
        return "Priority Queue is empty. Dequeue_min_priority failed."
    
    n = priority_queue['n']
    min_priority = priority_queue['data'][priority_queue['front']][1]
    
    # Checking the lowest priority:
    for i in range(n):
        temp = dequeue(priority_queue)
        if temp[1] < min_priority:
            min_priority = temp[1]
        enqueue_priority(priority_queue, temp[0], temp[1])
    
    # Checking the lowest priority element: 
    for j in range(n):
        temp = dequeue(priority_queue)
        if temp[1] == min_priority:
            element = temp
            break
        enqueue_priority(priority_queue, temp[0], temp[1])
                  
    return element

# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    if is_empty(priority_queue):
        return "Priority Queue is empty. Dequeue_min_priority failed."
        
    n = priority_queue['n']
    min_priority = priority_queue['data'][priority_queue['front']][1]
        
    for i in range(n):
        temp = dequeue(priority_queue)
        if temp[1] < min_priority:
            min_priority = temp[1]
        enqueue_priority(priority_queue, temp[0], temp[1])
        
    for j in range(n):
        temp = dequeue(priority_queue)
        if temp[1] == min_priority:
            element = temp[1]
        enqueue_priority(priority_queue, temp[0], temp[1])
        
    return element

# Function to process the calls:
def CallSimulator(callQueue, agentQueue) -> dict:

    # Simulation parameters
    Simulation = True
    currentTime = 0

    # Create a queue to store the call log
    callLog = create_queue(callQueue['size'])

    while Simulation:
        
        if is_empty(callQueue):
            Simulation = False
        
        else:
            
            for i in range(callQueue['n']):
                
                if is_empty(callQueue):
                    break
                
                call = dequeue(callQueue)
                agent = dequeue_min_priority(agentQueue)

                # Assigning agent to a call:
                if call[0] <= currentTime and agent[1] <= currentTime:
                    enqueue_priority(agentQueue, agent[0], agent[1] + call[2])
                    enqueue(callLog, (call[1], currentTime, currentTime + call[2], currentTime - call[0]))
            
                else:
                    enqueue(callQueue, call)
                    enqueue_priority(agentQueue, agent[0], agent[1])
                    
                
        
        # Increment the current time for the next iteration
        currentTime += 1

    # Returning the queue containing the call log
    return callLog

# Main function to take input and return the final output:
def main(filename) -> list:
    with open(filename) as f :
        lines = f.readlines()
    input = []
    for line in lines :
        line = line.strip() # remove leading and trailing spaces
        tokens = line.split() # split the line into tokens
        input.append(tokens) # add the first token to the input list
    
    agentQueue = create_priority_queue(len(input[0]))
    
    for name in input[0]:
        enqueue_priority(agentQueue, name, 0)
    
    call_queue = create_queue(int(input[1][0]))
    
    for i in input[2:]:
        i[0] = int(i[0])
        i[2] = int(i[2])
        enqueue(call_queue, i)
    
    # Simulate call processing using CallSimulator
    call_log = CallSimulator(call_queue, agentQueue)

    # Return the call log data as a list
    return call_log['data']

print(main("Inputs/callcenter01.txt"))
print(main("Inputs/callcenter02.txt"))
