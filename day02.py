

class Game:
    def __init__(self, game_input_line):
        (game, pulls) = game_input_line.split(':')
        self.game_id = game.split(' ')[1]
        self.hands = pulls.split(';')
        self.game_color_mins = {'red': 0, 'green': 0, 'blue': 0}
        self.cube_mins()

    def is_game_possible(self):
        # for part 1
        limits = {'red': 12, 'green': 13, 'blue': 14}

        for hand in self.hands:
            cubes = [cubes.strip() for cubes in hand.split(',')]
            for cube_set in cubes:
                (cube_count, cube_color) = cube_set.split(" ")
                if int(cube_count) > limits[cube_color]:
                    return False

        return True

    def cube_mins(self):
        for hand in self.hands:
            cubes = [cubes.strip() for cubes in hand.split(',')]
            for cube_set in cubes:
                (cube_count, cube_color) = cube_set.split(" ")
                if int(cube_count) > self.game_color_mins[cube_color]:
                    self.game_color_mins[cube_color] = int(cube_count)

    def cube_min_power(self):
        power = 1
        for (game_color, color_value) in self.game_color_mins.items():
            power = power * color_value
        return power


def part01(day_input):
    # working, took about 30 mins to solve
    game_id_total = 0

    for game_line in day_input:
        this_game = Game(game_line)
        if this_game.is_game_possible():
            game_id_total += int(this_game.game_id)

    print(game_id_total)


def part02(day_input):
    # working, took about 30-45 mins
    power_sum = 0
    for game_line in day_input:
        this_game = Game(game_line)
        power_sum += this_game.cube_min_power()
    print(power_sum)
