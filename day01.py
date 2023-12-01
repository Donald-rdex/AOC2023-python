import re


def part01(day01_input_lines: list) -> None:
    # working
    regex = re.compile(r'\D')
    total_sum = 0
    for line in day01_input_lines:
        numline = regex.sub('', line)
        newNum = numline[0] + numline[-1]
        total_sum += int(newNum)
    print(total_sum)


def part02(day01_input_lines):
    # not yet working
    regex = re.compile(r'\D')
    number_replacement_re = [(re.compile(r'nine'), '9'),
                             (re.compile(r'eight'), '8'),
                             (re.compile(r'seven'), '7'),
                             (re.compile(r'six'), '6'),
                             (re.compile(r'five'), '5'),
                             (re.compile(r'four'), '4'),
                             (re.compile(r'three'), '3'),
                             (re.compile(r'two'), '2'),
                             (re.compile(r'one'), '1'),
                             ]
    total_sum = 0
    for line in day01_input_lines:
        new_line = line
        re_find_order = {}

        for (num_line_re, replacement) in number_replacement_re:
            if num_line_re.search(new_line) is not None:
                re_find_order[num_line_re.search(new_line).start()] = replacement
        re_sorted_find_order = sorted(re_find_order)

        replacements = [pair for pair in number_replacement_re if pair[1] in re_sorted_find_order]
        for (pair_re, replacement) in replacements:
            new_line = pair_re.sub(replacement, new_line)
            print(new_line)

        print(new_line)
        new_line = regex.sub('', line)
        newNum = new_line[0] + new_line[-1]
        print(newNum)
        total_sum += int(newNum)
    print(total_sum)
