import day01
import day02


if __name__ == '__main__':
    today = '02'

    if today == '02':
        input_file = f'problem_inputs/day{today}_input.txt'
        with open(input_file) as day_fp:
            day_input = day_fp.readlines()
            day_input = [f'{i}'.strip() for i in day_input]
            day02.part01(day_input)
            day02.part02(day_input)

    if today == '01':
        day01_input_file = 'problem_inputs/day01_input.txt'
        with open(day01_input_file) as day01fp:
            day01_input = day01fp.readlines()
            day01_input = [f'{i}'.strip() for i in day01_input]
            day01.part01(day01_input)
            day01.part02(day01_input)
