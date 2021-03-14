'''
See the problem description https://adventofcode.com/2020/day/4
'''

def count_passports():
    '''
    Count number of valid passports
    '''

    count = 0 
    f = open("input.txt", "r")
    raw_data = f.read()
    passports = raw_data.split('\n\n')
    for passport in passports:
        if (passport_has_fields(passport)):
            count += 1
    return count

def passport_has_fields(passport: str) -> bool:
    '''
    Validate a given passport; needs
    - byr (Birth Year)
    - iyr (Issue Year)
    - eyr (Expiration Year)
    - hgt (Height)
    - hcl (Hair Color)
    - ecl (Eye Color)
    - pid (Passport ID)
    *cid (Country ID)
    '''

    fields_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in fields_list:
        if field not in passport:
            return False
    return True

def count_valid_passports():
    '''
    Count number of valid passports
    '''

    count = 0 
    f = open("input.txt", "r")
    raw_data = f.read()
    passports = raw_data.split('\n\n')
    for passport in passports:
        if (passport_is_valid(passport)):
            count += 1
    return count

def passport_is_valid(passport: str) -> bool:
    if (valid_birth_year(passport) and 
        valid_issue_year(passport) and
        valid_expiration_year(passport) and 
        valid_height(passport) and
        valid_hair_color(passport) and 
        valid_eye_color(passport) and
        valid_passport_id(passport)):
        return True
    return False

def valid_birth_year(passport: str) -> bool:
    '''
    Validate birth year
    - byr (Birth Year) - four digits; at least 1920 and at most 2002
    '''
    if ('byr' not in passport):
        return False
    _, value = passport.split('byr:')
    value = value.strip()
    number = int(value.split(' ')[0].split('\n')[0])
    return len(str(number)) == 4 and number >= 1920 and number <= 2002

def valid_issue_year(passport: str) -> bool:
    '''
    Validate issue year
    - iyr (Issue Year) - four digits; at least 2010 and at most 2020
    '''
    if ('iyr' not in passport):
        return False
    _, value = passport.split('iyr:')
    value = value.strip()
    number = int(value.split(' ')[0].split('\n')[0])
    return len(str(number)) == 4 and number >= 2010 and number <= 2020

def valid_expiration_year(passport: str) -> bool:
    '''
    Validate expiration year
    - eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    '''
    if ('eyr' not in passport):
        return False
    _, value = passport.split('eyr:')
    value = value.strip()
    number = int(value.split(' ')[0].split('\n')[0])
    return len(str(number)) == 4 and number >= 2020 and number <= 2030

def valid_height(passport: str) -> bool:
    '''
    Validate height
    - hgt (Height) - a number followed by either cm or in:
        - If cm, the number must be at least 150 and at most 193
        - If in, the number must be at least 59 and at most 76
    '''
    if ('hgt' not in passport):
        return False
    _, value = passport.split('hgt:')
    value = value.strip()
    try:
        if ('cm' in value):
            number = int(value.split(' ')[0].split('\n')[0][:3])
            return number >= 150 and number <= 193
        elif ('in' in value):
            number = int(value.split(' ')[0].split('\n')[0][:2])
            return number >= 59 and number <= 76
        else:
            return False
    except ValueError:
        return False
    return False

def valid_hair_color(passport: str) -> bool:
    '''
    Validate hair color 
    - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    '''
    if ('hcl' not in passport):
        return False
    _, value = passport.split('hcl:')
    value = value.strip()
    hair_color = (value.split(' ')[0].split('\n')[0])
    try:
        int(hair_color[1:], 16)
    except ValueError:
        # hair color is likely not hexadecimal
        return False
    return len(hair_color) == 7 and hair_color[0] == '#'

def valid_eye_color(passport: str) -> bool:
    '''
    Validate eye color
    - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    '''
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ('ecl' not in passport):
        return False
    _, value = passport.split('ecl:')
    value = value.strip()
    color = (value.split(' ')[0].split('\n')[0])
    return color.strip() in eye_colors

def valid_passport_id(passport: str) -> bool:
    '''
    Validate passport ID
    - pid (Passport ID) - a nine-digit number, including leading zeroes
    '''
    if ('pid' not in passport):
        return False
    _, value = passport.split('pid:')
    value = value.strip()
    try:
        number = int(value.split(' ')[0].split('\n')[0])
    except ValueError:
        # This implies pid is not a number (maybe it's hexa, or a height, etc.)
        return False
    return len(str(number)) == 9

if __name__ == '__main__':
    solution = count_passports()
    print(solution)
    solution2 = count_valid_passports()
    print(solution2)