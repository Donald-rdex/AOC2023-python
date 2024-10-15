import re


def part01(speed_input):
    times = re.split(r'\s+', speed_input[0])[1:]
    distances = re.split(r'\s+', speed_input[1])[1:]

    for race in len(times):
        for poweruptime in (range(1, times[race])):
            time to travel = times[race] - poweruptime
