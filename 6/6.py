'''
Problem description available here https://adventofcode.com/2020/day/6
'''

import string

def count_yeses() -> int:
    '''
    Count all non-newline or space characters in a text file
    '''

    # Initialize file, count (rsf accumulator)
    f = open("input.txt", "r")
    raw_data = f.read()
    answers = raw_data.split('\n\n')
    total = 0

    for answer in answers:
        count = 0
        seen = []
        for c in answer:
            if c.isalnum() and c not in seen:
                count += 1
                seen.append(c)
        total += count
    return total

def count_common() -> int:
    '''
    Count all non-newline or space characters in a text file
    '''

    # Initialize file, count (rsf accumulator)
    f = open("input.txt", "r")
    raw_data = f.read()
    answers = raw_data.split('\n\n')
    total = 0

    # Loop through a group
    for answer in answers:
        # Get people in a group
        people = answer.split('\n')
        p_dict = {}
        # Loop through people in a group
        for person in people:
            print(person)
            for p in person:
                if p in p_dict.keys():
                    p_dict[p] = p_dict[p] + 1
                else:
                    p_dict[p] = 1
        # Increase total
        print(p_dict)
        for value in p_dict.values():
            if value >= len(people):
                total += 1
        print(total)
        # return total
    return total

if __name__ == '__main__':
    solution = count_yeses()
    print(solution)
    solution2 = count_common()
    print(solution2)