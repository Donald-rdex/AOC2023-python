import day01

if __name__ == '__main__':

    day01_input_file = 'problem_inputs/day01_input.txt'
    with open(day01_input_file) as day01fp:
        day01_input = day01fp.readlines()
        day01_input = [f'{i}'.strip() for i in day01_input]
        day01.part01(day01_input)
        day01.part02(day01_input)
