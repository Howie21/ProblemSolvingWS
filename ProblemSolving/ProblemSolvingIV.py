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

test_string1 = 'aabbaa'
test_string2 = 'abaababba'

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
    value = ""
    if number >= number2:
        value = number - number2
    elif number2 > number:
        value = number2 - number
    
    if value >= 13:
        value = value * 2
    return value 


# absolute_diff(-12, 7)

test_string3 = 'adefb'
test_string4 = 'adesdfb'

def check_seperation_of(character1, character2, string_variable, space_limit):
    string_to_list = list(string_variable)
    limitation = space_limit + 2
    counter = 0
    for letter in string_to_list:
        if letter == character1:
            for letter2 in string_to_list:
                counter += 1
                if letter == character1 and letter2 == character2:
                    if counter == limitation:
                        print(f'{character1} is {space_limit} spaces away from {character2}')
                        return
                    else:
                        print(f'{character1} is not {space_limit} spaces away from {character2}, \nbut {character1} is {counter} spaces away from {character2}')


# check_seperation_of("a", "b", test_string4, 3)

equal_ts_and_ps = "ttttaaaapppp"
non_equal_ts_and_ps = 'tttaaaaappppp'

def same_amount_check(string, character1, character2):
    character1_counter = 0
    character2_counter = 0
    for letter in string:
        if letter == character1:
            character1_counter += 1
        elif letter == character2:
            character2_counter += 1
    if character1_counter == character2_counter:
        print(f"There are an equal number of {character1}'s and {character2}'s")
    else:
        print(f"There are not an equal number of {character1}'s and {character2}'s \n")

# same_amount_check(non_equal_ts_and_ps, "t", "p")


number_string = "19234536"
number_and_letters = 'asdf234526sdgdf'

def sum_of_all_digits(string):
    sum = 0
    for number in string:
        if number.isdigit():
            sum += int(number)
    print(sum)


# sum_of_all_digits(number_and_letters)

# proper or improper fractions

# Pig Latin translation

#Solving issues with List ----------------- 

list_of_numbers = [5, 3, 54, 6, 4, 2, 6, 34]

def largest_element(list_name):
    counter = 0
    highest_value = list_name[counter]
    for number in list_name:
        if number > highest_value:
            counter = list_name.index(number)
    return highest_value

# print(largest_element(list_of_numbers))


given_list = [7, 17, 77, 50, 60, 22, 38]
given_target = 55


def return_numbers(some_list, some_target):
    for number in some_list:
        for number2 in some_list:
            if number + number2 == some_target:
                print(number, number2)
            

return_numbers(given_list, given_target)

