import random
 
RPS = ('rock', 'paper', 'scissors')
WINS = ('Rock breaks scissors.', 'Paper wraps rock.', 'Scissors cut paper.')
 
 
def ask_player():
    """
   Returns int. 0: rock, 1: paper, 2: scissors, -1: quit
   """
    print('Choose (r)ock, (p)aper, (s)cissors or (q)uit game.')
    while True:
        ans = input('> ').lower()[0]
        if ans not in ('r', 'p', 's', 'q'):
            print("I don't understand the answer, try again.")
            continue
        elif ans == 'q':
            return -1
        else:
            return {'r': 0, 'p': 1, 's': 2}[ans]
 
 
def rps():
    """
   Simple rock paper scissors game
   """
    win = 0
    loss = 0
    games = 0
    print('\n       Welcome to ROCK PAPER SCISSORS GAME')
    while True:
        player_choice = ask_player()
        if player_choice == -1:
            break
        computer_choice = random.randrange(3)
        games += 1
 
        print('\nYou picked {},'.format(RPS[player_choice].upper()), end='')
        print(' computer picks {}.'.format(RPS[computer_choice].upper()))
 
        diff = (computer_choice - player_choice) % 3
 
        if diff == 2:
            print(WINS[player_choice] + ' You win!')
            win += 1
        elif diff == 1:
            print(WINS[computer_choice] + ' You loose.')
            loss += 1
        else:
            print("It's a tie. Nobody wins.")
 
        # I like everything aligned :-)
        spacing = 29 - len(str(games)) - len(str(win)) - len(str(loss))
        print('\nGames: {}{}'
              'You {}:{} Computer'.format(games, spacing*' ', win, loss))
        print('-' * 50, end='\n\n')
 
    print('\nThanks for playing.\nAfter {} games '.format(games), end='')
    if win > loss:
        print('you win with score {}.'.format(win))
    elif win < loss:
        print('computer wins with score {}.'.format(loss))
    else:
        print("it's a tie. You and computer have score {}.".format(win))
 
if __name__ == "__main__": rps()