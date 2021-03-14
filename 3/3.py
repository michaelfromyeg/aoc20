'''
See the problem description https://adventofcode.com/2020/day/3
'''

def count_trees() -> int:
    '''
    Count the number of trees encountered on (3, 1) path
    '''
    count = 0
    x = 0
    y = 0 # y represents rows to skip (this will become important later!)
    f = open("input.txt", "r")
    for val in f:

        # Remove white space
        val = val.strip()

        # Compute the maximum allowable value of x
        max_val = len(val)

        # Count a tree
        if (val[x] == '#'):
            count += 1
        
        # Increment x, y 
        x, y = x + 3, y + 0

        if (x >= max_val):
            x = x % max_val
    return count

def count_trees_generic(dx: int, dy: int) -> int:
    '''
    Count trees on a path (dx, dy)
    '''
    count = 0
    x = 0
    y = 0
    f = open("input.txt", "r")
    for val in f:

        # Skip rows
        if (y > 0):
            y -= 1
            continue

        # Remove white space
        val = val.strip()

        # Compute the maximum allowable value of x
        max_val = len(val)

        # Count a tree
        if (val[x] == '#'):
            count += 1
        
        # Increment x, y 
        x, y = x + dx, y + (dy - 1)

        # Wrap x back around
        if (x >= max_val):
            x = x % max_val
    return count

if __name__ == '__main__':
    solution = count_trees()
    print(solution)

    x1 = count_trees_generic(1, 1)
    x2 = count_trees_generic(3, 1)
    x3 = count_trees_generic(5, 1)
    x4 = count_trees_generic(7, 1)
    x5 = count_trees_generic(1, 2)

    print(x1 * x2 * x3 * x4 * x5)