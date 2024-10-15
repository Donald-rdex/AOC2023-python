
class Y2020D02:
    pwd_input = []

    def __init__(self, input_list):
        for i in input_list:
            (rules, pwd) = i.split(":")
            (minmax, ltr) = rules.split(" ")
            (min_ltr, max_ltr) = minmax.split("-")

            self.pwd_input.append((int(min_ltr), int(max_ltr), ltr.strip(), pwd.strip(), i))

    def day01(self):
        correct_passwords = 0
        for potential_word in self.pwd_input:
            filtered_word_count = potential_word[3].count(potential_word[2])
            if potential_word[0] <= filtered_word_count <= potential_word[1]:
                correct_passwords += 1

        print(correct_passwords)

    def day02(self):
        correct_passwords = 0
        pos1 = False
        pos2 = False
        for pword in self.pwd_input:
            if pword[3][pword[0]-1] == pword[2]:
                pos1 = True
            if pword[3][pword[1]-1] == pword[2]:
                pos2 = True
            if pos1 ^ pos2:
                correct_passwords += 1
                print(pword[0], pword[1], "s:", pword[3][pword[0]-1], "e:", pword[3][pword[1]-1], "ltr:", pword[2], pword[3])
            pos1 = False
            pos2 = False

        print(correct_passwords)
