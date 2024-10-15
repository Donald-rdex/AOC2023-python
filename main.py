import day01
import day02
import day03
import day04
import day05

from y2020_d02 import Y2020D02


if __name__ == '__main__':
    today = '2020'

    input_file = f'problem_inputs/aoc_2020_02_input.txt'
    with open(input_file) as day_fp:
        day_input = day_fp.readlines()
        day_input = [f'{i}'.strip() for i in day_input]

        aoc2020d2 = Y2020D02(day_input)
        aoc2020d2.day01()
        aoc2020d2.day02()


    if today == '05' or today == '06':
        # input_file = f'problem_inputs/day{today}_input.txt'
        input_file = f'problem_inputs/test_input.txt'

        with open(input_file) as day_fp:
            day_input = day_fp.readlines()
            day_input = [f'{i}'.strip() for i in day_input]

            if today == '05':
                day05.part01(day_input)
                day05.part02(day_input)
            if today == '06':
                day05.part01(day_input)
                day05.part02(day_input)

    if today == '04':
        input_file = f'problem_inputs/day{today}_input.txt'
        # input_file = f'problem_inputs/test_input.txt'
        with open(input_file) as day_fp:
            day_input = day_fp.readlines()
            day_input = [f'{i}'.strip() for i in day_input]
            day04.part01(day_input)
            day04.part02(day_input)

    if today == '03':
        input_file = f'problem_inputs/day{today}_input.txt'
        # input_file = f'problem_inputs/day{today}_test.txt'
        with open(input_file) as day_fp:
            day_input = day_fp.readlines()
            day_input = [f'{i}'.strip() for i in day_input]
            day03.part01(day_input)
            day03.part02(day_input)

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
