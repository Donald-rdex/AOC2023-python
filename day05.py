import re


class FarmMaps:
    def __init__(self):
        self.s2s = []
        self.s2f = []
        self.f2w = []
        self.w2l = []
        self.l2t = []
        self.t2h = []
        self.h2l = []


class Seeds:
    def __init__(self):
        self.seeds = []


def parse_input(input_list):
    seeds = Seeds()
    my_farm = FarmMaps()

    map_type = None

    for line in input_list:
        s2s_map = line.strip().split(' ')
        if re.match(r'seeds: ', line):
            seeds.seeds = [int(seed) for seed in line.strip().split() if seed.isnumeric()]
        # elif line and re.match(r'\d+ \d+ \d+', line):
        #     s2s_map = list(map(int, s2s_map))

        if re.match(r'seed-to-soil map:', line):
            map_type = 'seed-to-soil map:'
        if re.match(r'soil-to-fertilizer map:', line):
            map_type = 'soil-to-fertilizer map:'
        if re.match(r'fertilizer-to-water map:', line):
            map_type = 'fertilizer-to-water map:'
        if re.match(r'water-to-light map:', line):
            map_type = 'water-to-light map:'
        if re.match(r'light-to-temperature map:', line):
            map_type = 'light-to-temperature map:'
        if re.match(r'temperature-to-humidity map:', line):
            map_type = 'temperature-to-humidity map:'
        if re.match(r'humidity-to-location map:', line):
            map_type = 'humidity-to-location map:'

        if line and re.match(r'\d+ \d+ \d+', line):
            s2s_map = list(map(int, s2s_map))
            map_range = (s2s_map[1], s2s_map[0], s2s_map[1] + s2s_map[2], s2s_map[0] + s2s_map[2])

            if map_type == 'seed-to-soil map:':
                my_farm.s2s.append(map_range)
            if map_type == 'soil-to-fertilizer map:':
                my_farm.s2f.append(map_range)
            if  map_type == 'fertilizer-to-water map:':
                my_farm.f2w.append(map_range)
            if map_type == 'water-to-light map:':
                my_farm.w2l.append(map_range)
            if map_type == 'light-to-temperature map:':
                my_farm.l2t.append(map_range)
            if map_type == 'temperature-to-humidity map:':
                my_farm.t2h.append(map_range)
            if map_type == 'humidity-to-location map:':
                my_farm.h2l.append(map_range)

    return seeds, my_farm


def part01(input_lines):
    (seeds, farm_map) = parse_input(input_lines)
    lowest_location = -1
    for seed in seeds.seeds:
        for s2s in farm_map.s2s:
            if s2s[0] <= seed <= s2s[2]:
                soil = s2s[1] + (seed - s2s[0])
                break
            soil = seed
        for s2f in farm_map.s2f:
            if s2f[0] <= soil <= s2f[2]:
                fertilizer = s2f[1] + (soil - s2f[0])
                break
            fertilizer = soil
        for f2w in farm_map.f2w:
            if f2w[0] <= fertilizer <= f2w[2]:
                water = f2w[1] + (fertilizer - s2f[0])
                break
            water = fertilizer
        for w2l in farm_map.w2l:
            if w2l[0] <= water <= w2l[2]:
                light = w2l[1] + (water - w2l[0])
                break
            light = water
        for l2t in farm_map.l2t:
            if l2t[0] <= light <= l2t[2]:
                temperature = l2t[1] + (light - l2t[0])
                break
            temperature = light
        for t2h in farm_map.t2h:
            if t2h[0] <= temperature <= t2h[2]:
                humidity = t2h[1] + (temperature - t2h[0])
                break
            humidity = temperature
        for h2l in farm_map.h2l:
            if h2l[0] <= humidity <= h2l[2]:
                location = h2l[1] + (humidity - h2l[0])
                break
            location = humidity

        if lowest_location == -1:
            lowest_location = location
        elif location < lowest_location:
            lowest_location = location

    print(lowest_location)


def part02(input_lines):
    pass
