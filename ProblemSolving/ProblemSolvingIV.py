import re

#Print 20 leap years

def whats_next_leap_year(current_year):
    the_next_leap_year = current_year
    while the_next_leap_year % 4 != 0:
        the_next_leap_year += 1
    return the_next_leap_year

def how_many_leaps(int):
    value = int *4
    return value

def print_leap_years(year, number_of_leaps):
    next_leap_year = whats_next_leap_year(year)
    next_20 = how_many_leaps(number_of_leaps)
    end_loop = year + (next_20)
    while next_leap_year != end_loop:
        next_leap_year = next_leap_year + 4
        print(next_leap_year)
    print('That is the number of leap years asked for!')

#longest palindromic substring 

test_string1 = 'aabbaa'
test_string2 = 'abaababba'


def reverse_string(string):
    result = string[::-1]
    return result

def check_palindrome(input):
    proper_input = input.lower()
    input_reversed = reverse_string(proper_input)
    if proper_input == input_reversed:
        return True
    elif proper_input != input_reversed:
        return False

#recursion

def longest_palindromic_substring(string):
    string = string.lower()
    string_as_list = list(string)
    palindromic_string_list = []
    length_of_list = len(palindromic_string_list) -1
    for letter in string:
        palindromic_string_list.append(letter)
        
    answer = "".join(palindromic_string_list)
    return answer

# longest_palindromic_substring(test_string2)

def absolute_diff(number, number2):
    if number >= number2:
        value = number - number2
        return 
    elif number2 > number:
        value = number2 - number
        return value

