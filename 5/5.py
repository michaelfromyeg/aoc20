'''
See the problem description https://adventofcode.com/2020/day/5
'''

import math

ROW_MAX = 127
COL_MAX = 7

def get_highest_id() -> int:
    '''
    Return the highest ID in input.txt
    '''
    
    id_max = -99999
    f = open("input.txt", "r")

    for val in f:

        # Initialize seat values
        ru = 127
        rl = 0
        cu = 7
        cl = 0
        row = -1
        col = -1

        # Strip input (to remove \n)
        val = val.strip()

        # Loop for rows
        for i in range(7):
            if val[i] == 'F':
                ru = math.floor((rl + ru) / 2)
            elif val[i] == 'B':
                rl = math.ceil((rl + ru) / 2)
            else:
                raise Exception
            # Last iteration
            if (i == 7 - 1):
                row = ru if val[i] == 'F' else rl

        # Loop for columns
        for i in range(7, len(val)):
            if val[i] == 'L':
                cu = math.floor((cl + cu) / 2)
            elif val[i] == 'R':
                cl = math.ceil((cl + cu) / 2)
            else:
                raise Exception
            # Last iteration
            if (i == len(val) - 1):
                col = cu if val[i] == 'R' else cl
        
        # Compute the ID and update max
        id_value = row * 8 + col
        if (id_value > id_max):
            id_max = id_value
    
    # After looping through each input, return max
    return id_max

def get_ids():
    '''
    Return all seat IDs in a list
    '''
    
    ids = []
    f = open("input.txt", "r")

    for val in f:

        # Initialize seat values
        ru = 127
        rl = 0
        cu = 7
        cl = 0
        row = -1
        col = -1

        # Strip input (to remove \n)
        val = val.strip()

        # Loop for rows
        for i in range(7):
            if val[i] == 'F':
                ru = math.floor((rl + ru) / 2)
            elif val[i] == 'B':
                rl = math.ceil((rl + ru) / 2)
            else:
                raise Exception
            # Last iteration
            if (i == 7 - 1):
                row = ru if val[i] == 'F' else rl

        # Loop for columns
        for i in range(7, len(val)):
            if val[i] == 'L':
                cu = math.floor((cl + cu) / 2)
            elif val[i] == 'R':
                cl = math.ceil((cl + cu) / 2)
            else:
                raise Exception
            # Last iteration
            if (i == len(val) - 1):
                col = cu if val[i] == 'R' else cl
        
        # Compute the ID and update max
        id_value = row * 8 + col
        ids.append(id_value)
    
    # After looping through each input, return max
    return ids

def find_missing(ids) -> int:
    '''
    Return the missing ID using properties of sets
    '''
    ids = sorted(ids)
    start, end = ids[0], ids[-1]
    missing = sorted(set(range(start, end + 1)).difference(ids))[0]
    return missing

if __name__ == '__main__':
    highest = get_highest_id()
    print(highest)
    ids = get_ids()
    missing = find_missing(ids)
    print(missing)