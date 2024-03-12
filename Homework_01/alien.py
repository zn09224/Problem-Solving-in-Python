import list_adt as listadt

# Creating the dictionary to store messages from aliens and other useful data:
def create_alien() -> dict[str, any]:
    alien = {
        'messages': listadt.create_list(100),
        'max_S': 0,     
        'min_S': 0,
        'R': 50,
    }
    return alien

# Function to add messages to the messages queue:
def add(seq: int, msg: str, alienList: dict):
    
    # Condition for first messages:
    if alienList['min_S'] == 0:
        alienList['min_S'] = alienList['max_S'] = seq
        listadt.insert_last((msg, alienList['R']), alienList['messages'])
    
    # Condition for messages having smallest sequence number:
    elif seq < alienList['min_S']:
                
        alienList['R'] = alienList['R'] - 1
        listadt.insert_last((msg, alienList['R']), alienList['messages'])
        alienList['min_S'] = seq
    
    #Condtion for messages having max sequence number:       
    elif seq > alienList['max_S']:
                
        alienList['R'] = alienList['R'] + 1
        listadt.insert_last((msg, alienList['R']), alienList['messages'])
        alienList['max_S'] = seq
        
# Function to delete the last recieved message:       
def delete(seq: int, msg: str, alienList: dict):
    
    listadt.remove_last(alienList['messages'])
    alienList['R'] -= 1
    
# Function to sort the messages accordingly:
def get_messages(alienList: dict) -> list[str]:
        
    temp01 = listadt.get_first(alienList['messages'])
    max = temp01[1]
    
    # Getting the highest assigned number:
    for i in range(listadt.length(alienList['messages'])):
        
        temp = listadt.get_first(alienList['messages'])
        
        if temp[1] > max:
            max = temp[1]
        
        listadt.remove_first(alienList['messages'])
        listadt.insert_last(temp, alienList['messages'])
    
    max = max + 1
    
    temp_array = [None for i in range(max)]     # Array with size equal to the highest assigned number
    
    # Putting messages in the temp_array on the index of their assigned number:
    for j in range(listadt.length(alienList['messages'])):
        
        temp = listadt.get_first(alienList['messages'])
        print(temp[1])
        temp_array[temp[1]] = temp
        
        listadt.remove_first(alienList['messages'])
        listadt.insert_last(temp, alienList['messages'])
    
    count = 0
    
    # Getting the number of elements in temp_array:
    for k in range(max):
        
        if temp_array[k] != None:
            count += 1
    
    output_array = [None for i in range(count)]     # Final sorted list of messages
    
    ind = 0
    
    # Putting messages in output_array
    for l in range(max):
        
        if temp_array[l] != None:
            output_array[ind] = temp_array[l][0] 
            ind += 1
     
    return output_array

def main(filename) -> list[str]:
    
    messages = create_alien()
    
    message_number = 1
    
    with open(filename) as f:
        lines = f.readlines()
     
    for line in lines:
        
        line = line.strip() # remove leading and trailing spaces
        message = line.split() # split the line into tokens
        
        if int(message[0]) == 0:
            break
        
        # Condition to check if sequence number is negative:
        elif int(message[0]) < 0:
            delete(prev_seq, prev_message, messages)
            continue        # Go to the next iteration to read the next message:
        
        # Go to the next iteration to read the next message if the sequence number is between the max and min:
        elif int(message[0]) > messages['min_S'] and int(message[0]) < messages['max_S']:
            continue
        
        # Call the add function to add the messages to message queue
        else:
            add(int(message[0]), message[1], messages)
        
        prev_seq = int(message[0])      # Keeping track of the sequence number of last recieved message
        prev_message = message[1]       # Keeping track of the message string of last recieved message
            
    output = get_messages(messages)
    
    s = ""
    
    for i in output:
        s = s + i + " "
     
    s = s[0:-1]
    
    return s                        

main("Inputs/alien01.txt")
main("Inputs/alien02.txt")