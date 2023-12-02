

class Game:
    def __init__(self, game_input_line):
        (game, pulls) = game_input_line.split(':')
        self.game_id = game.split(' ')[1]
        self.hands = pulls.split(';')

    def is_game_possible(self):
        limits = {'red': 12, 'green': 13, 'blue': 14}

        for hand in self.hands:
            cubes = [cubes.strip() for cubes in hand.split(',')]
            for cube_set in cubes:
                (cube_count, cube_color) = cube_set.split(" ")
                if int(cube_count) > limits[cube_color]:
                    return False

        return True


def part01(day_input):
    # working, took about 30 mins to solve
    game_id_total = 0

    for game_line in day_input:
        this_game = Game(game_line)
        if this_game.is_game_possible():
            game_id_total += int(this_game.game_id)

    print(game_id_total)



def part02(day_input):
    pass
