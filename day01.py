import re


def part01(day01_input_lines: list) -> None:
    # working
    regex = re.compile(r'\D')
    total_sum = 0
    for line in day01_input_lines:
        num_line = regex.sub('', line)
        new_num = num_line[0] + num_line[-1]
        total_sum += int(new_num)
    print(total_sum)


def part02(day01_input_lines):
    # after a lot of stop/start... working
    digit_re = re.compile(r'\d')
    non_digit_re = re.compile(r'\D')
    number_replacement_re = [('nine', re.compile(r'nine'), '9'),
                             ('eight', re.compile(r'eight'), '8'),
                             ('seven', re.compile(r'seven'), '7'),
                             ('six', re.compile(r'six'), '6'),
                             ('five', re.compile(r'five'), '5'),
                             ('four', re.compile(r'four'), '4'),
                             ('three', re.compile(r'three'), '3'),
                             ('two', re.compile(r'two'), '2'),
                             ('one', re.compile(r'one'), '1'),
                             ]
    total_sum = 0
    for line in day01_input_lines:
        new_line = line

        found_number = ''
        index = 0
        for possible_digit in new_line:
            if digit_re.match(possible_digit):
                found_number += possible_digit
            else:
                for number_tup in number_replacement_re:
                    if number_tup[1].match(new_line[index:]):
                        found_number += number_tup[2]
            index += 1

        found_number = non_digit_re.sub('', found_number)
        number_pair = found_number[0] + found_number[-1]
        total_sum += int(number_pair)
    print(total_sum)
