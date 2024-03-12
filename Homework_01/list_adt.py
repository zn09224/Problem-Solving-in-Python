def create_list(size):

    return {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': -1,    # Index for circular storage of elements
    }

def is_empty(listADT):
    if listADT['n'] == 0:
        return True
    else:
        return False


def is_full(listADT):
    if listADT['n'] == listADT['size']:
        return True
    else:
        return False


def get(i, listADT):
    
    if is_empty(listADT):
        return "get failed. DEqueue is empty."

    s = None
        
    for k in range(listADT['n']):
        temp = get_first(listADT)
        if k == i:
            s = temp
        remove_first(listADT)
        insert_last(temp, listADT)
        
    return s
               

def set(i, e, listADT):
    
    if is_empty(listADT):
        return "set failed. DEqueue is empty."
        
    for k in range(listADT['n']):
        temp = get_first(listADT)
        if k == i:
            temp = e
        remove_first(listADT)
        insert_last(temp, listADT)


def length(listADT):
    return listADT['n']


def add(i, e, listADT):
    
    if is_full(listADT):
        return "add failed. DEqueue is full."
    
    for k in range(listADT['n']):
        temp = get_first(listADT)
        if k == i:
            insert_last(e, listADT)
        remove_first(listADT)
        insert_last(temp, listADT)
   

def remove(i, listADT):
    
    if is_empty(listADT):
        return "remove failed. DEqueue is empty."
    
    for k in range(listADT['n']):
        temp = get_first(listADT)
        remove_first(listADT)
        if k != i:
            insert_last(temp, listADT)
    

def insert_last(e, listADT):
    
    if is_full(listADT):
        return "Insert_last failed. DEqueue is full."
    
    if is_empty(listADT):
        listADT['i'] = 0
        
    listADT['data'][(listADT['i'] + listADT['n']) % listADT['size']] = e
    
    listADT['n'] += 1 


def remove_last(listADT):
    
    if is_empty(listADT):
        return "remove_last failed. DEqueue is empty."
    
    listADT['data'][(listADT['i'] + listADT['n'] - 1) % listADT['size']] = None
    
    listADT['n'] -= 1

    
def insert_first(e, listADT):
    
    if is_full(listADT):
        return "insert_first failed. DEqueue is full."
    
    listADT['i'] = (listADT['i'] - 1) % listADT['size']
    listADT['data'][listADT['i']] = e
    listADT['n'] += 1
        

def remove_first(listADT):
    
    if is_empty(listADT):
        return "remove_first failed. DEqueue is empty."
    
    listADT['data'][listADT['i']] = None
    listADT['i'] = (listADT['i'] + 1) % listADT['size']
    listADT['n'] -= 1


def get_first(listADT):
    
    return listADT['data'][listADT['i']]


def get_last(listADT):
    
    return listADT['data'][(listADT['i'] + listADT['n'] - 1) % listADT['size']]