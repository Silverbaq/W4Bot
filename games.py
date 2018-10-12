from random import randint


class RockPaperScissors(object):
    items = ['rock', 'paper', 'scissors']

    def choice_hand(self):
        choice = self.items[randint(0, 2)]
        return choice

    def check_outcome(self, hand, choice):
        if hand not in self.items:
            return 'Not a valid choice'
        elif hand == choice:
            return '{0} vs {1}: DRAW'.format(hand, choice)
        elif hand == self.items[0]:
            if choice == self.items[1]:
                return '{0} vs {1}: You lose!'.format(hand, choice)
            else:
                return '{0} vs {1}: You win!'.format(hand, choice)
        elif hand == self.items[1]:
            if choice == self.items[2]:
                return '{0} vs {1}: You lose!'.format(hand, choice)
            else:
                return '{0} vs {1}: You win!'.format(hand, choice)
        elif hand == self.items[2]:
            if choice == self.items[0]:
                return '{0} vs {1}: You lose!'.format(hand, choice)
            else:
                return '{0} vs {1}: You win!'.format(hand, choice)

    def play(self, hand):
        choice = self.choice_hand()
        result = self.check_outcome(hand.lower(), choice)
        return result