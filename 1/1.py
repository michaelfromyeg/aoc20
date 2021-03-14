'''
See the problem description https://adventofcode.com/2020/day/1
'''

MAIN_TARGET = 2020

def two_nums(target: int, vals) -> int:
    '''
    Return two numbers that sum to 2020
    '''
    seen = []
    seen.append(vals)
    f = open("input.txt", "r")
    for val in f:
        curr = int(val)
        addend = target - curr
        if (addend in seen):
            return addend * curr
        else:
            seen.append(curr)
    raise AssertionError

def three_nums(target: int) -> int:
    '''
    Return three numbers that sum to 2020
    '''
    seen = []
    partial_sums = []
    f = open("input.txt", "r")
    for val in f:
        curr = int(val)
        addend = target - curr
        if (addend in partial_sums):
            result = two_nums(addend, seen)
            return result * curr
        else:
            for s in seen:
                partial_sums.append(s + curr)
            seen.append(curr)
    raise AssertionError

if __name__ == '__main__':
    two = two_nums(MAIN_TARGET, [])
    print(two)
    three = three_nums(MAIN_TARGET)
    print(three)
