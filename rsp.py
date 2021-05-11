from random import randint

play = ['Rock', 'Scissors', "Paper"]
computer = play[randint(0, len(play))]
print('Computer: {}'.format(computer))

player = 'Paper'
print('Player: {}'.format(player))
