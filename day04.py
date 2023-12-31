

class LottoCard:
    def __init__(self, card_number, list_of_winning_numbers, list_of_played_numbers):
        self.card_number = card_number
        self.winning_numbers = list_of_winning_numbers
        self.played_number = list_of_played_numbers
        self.copies = 1

    def points(self):
        card_points = 0
        for win in self.winning_numbers:
            if win in self.played_number:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points * 2
        return card_points

    def wins(self):
        # variation on part1 but with counts
        wins = 0
        for win in self.winning_numbers:
            if win in self.played_number:
                wins += 1
        return wins


def part01(input_lines):
    # working!
    cards = []
    total_points = 0
    for game_card in input_lines:
        (card, play_line) = game_card.split(":")
        card_number = card.split(' ')[-1]
        (winning_nums, played_nums) = play_line.split('|')
        winning_list = [wn for wn in winning_nums.strip().split(" ") if wn.isnumeric()]
        played_list = [pn for pn in played_nums.strip().split(" ") if pn.isnumeric()]
        new_game_card = LottoCard(card_number, winning_list, played_list)
        # print(new_game_card.points())
        total_points += new_game_card.points()
        cards.append(new_game_card)
    # print(total_points)
    return cards


def part02(input_lines):
    # working!
    cards = part01(input_lines)

    for (index, card) in enumerate(cards):
        if (wins := card.wins()) > 0:
            card_idx = index + 1
            while wins > 0:
                cards[card_idx].copies += card.copies
                wins -= 1
                card_idx += 1

    print(sum([card.copies for card in cards]))
