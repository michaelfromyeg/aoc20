'''
See the problem description https://adventofcode.com/2020/day/2
'''

def error_one() -> int:
    '''
    Return the number of acceptable passwords
    '''
    count = 0
    f = open("input.txt", "r")
    for val in f:
        condition, password = val.split(':')
        amounts, letter = condition.split(' ')
        lower_bound, upper_bound = amounts.split('-')
        
        num = 0
        for c in password:
            if c == letter:
                num += 1
        if num >= int(lower_bound) and num <= int(upper_bound):
            count += 1
    return count

def error_two() -> int:
    '''
    Return iff one of the password indices, password[lower_bound] or password[upper_bound], matches letter
    '''
    count = 0
    f = open("input.txt", "r")
    for val in f:
        condition, password = val.split(':')
        password = password.strip()
        amounts, letter = condition.split(' ')
        lower_bound, upper_bound = amounts.split('-')
        if ((password[int(lower_bound)-1] == letter) != (password[int(upper_bound)-1] == letter)): # like xor
            count += 1
    return count
        
if __name__ == '__main__':
    solution = error_one()
    print(solution)
    solution2 = error_two()
    print(solution2)