

class EnginePart:
    def __init__(self, part_number, part_location_idx, part_location_line, part_symbol, part_sym_line, part_sym_idx):
        self.part_number = part_number
        self.part_location_idx = part_location_idx
        self.part_location_line = part_location_line
        self.part_symbol = part_symbol
        self.part_sym_line = part_sym_line
        self.part_sym_idx = part_sym_idx

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def part01(day_input):
    # not working yet.
    # read each digit of a part number, until next '.', storing indexes of numbers in the line
    # store the number, the starting location, the part location and the part symbol.
    engine_parts = []
    line_number = 0
    for line in day_input:
        current_part = EnginePart(part_number=None, part_location_idx=None, part_location_line=None,
                                  part_symbol=None, part_sym_line=None, part_sym_idx=None)
        found_part = False
        for idx in range(len(line)):
            if line[idx].isdigit() and line[idx] in '0123456789':
                if found_part is False:
                    current_part.part_number = line[idx]
                    current_part.part_location_idx = idx
                    current_part.part_location_line = line_number
                    found_part = True
                else:
                    current_part.part_number += line[idx]
                    found_part = True

            else:
                if found_part:
                    engine_parts.append(current_part)
                    current_part = EnginePart(part_number=None, part_location_idx=None, part_location_line=None,
                                              part_symbol=None, part_sym_line=None, part_sym_idx=None)
                found_part = False
            if found_part:
                print(f'{bcolors.OKBLUE}{line[idx]}{bcolors.ENDC}', end='')
            else:
                if line[idx] != '.':
                    print(f'{bcolors.OKGREEN}{line[idx]}{bcolors.ENDC}', end='')
                else:
                    print(f'{line[idx]}', end='')
        print('')
        line_number += 1

    ep_index = 0
    # last_line=0
    for ep in engine_parts:
        # having found all engine parts, search for symbols around the part number
        starting_line = ep.part_location_line
        starting_idx = ep.part_location_idx

        # up, down, and all around...
        line_above = starting_line - 1
        if line_above < 0:
            line_above = 0
        line_below = starting_line + 1
        if line_below >= len(day_input):
            line_below = starting_line

        col_before = starting_idx - 1
        if col_before < 0:
            col_before = 0
        col_after = starting_idx + len(ep.part_number) + 1
        if col_after >= len(day_input[starting_line]):
            col_after = len(day_input[starting_line])

        for curr_col in range(col_before, col_after):
            line_above_ch = day_input[line_above][curr_col]
            line_curr_ch = day_input[starting_line][curr_col]
            line_below_ch = day_input[line_below][curr_col]
            if not line_above_ch.isdigit() and line_above_ch != '.':
                engine_parts[ep_index].part_symbol = line_above_ch
                engine_parts[ep_index].part_sym_line = line_above
                engine_parts[ep_index].part_sym_idx = curr_col
                break
            if not line_curr_ch.isdigit() and line_curr_ch != '.':
                engine_parts[ep_index].part_symbol = line_curr_ch
                engine_parts[ep_index].part_sym_line = starting_line
                engine_parts[ep_index].part_sym_idx = curr_col
                break
            if not line_below_ch.isdigit() and line_below_ch != '.':
                engine_parts[ep_index].part_symbol = line_below_ch
                engine_parts[ep_index].part_sym_line = line_below
                engine_parts[ep_index].part_sym_idx = curr_col
                break
        ep_index += 1

    part_sum = 0
    for ep in engine_parts:
        if ep.part_symbol is not None:
            # print(f'{ep.part_number}: {ep.part_symbol}')
            part_sum += int(ep.part_number)
        # else:
            # print(f'{ep.part_number}: {ep.part_location_line}: ...')

    print(part_sum)

def part02(day_input):
    pass
