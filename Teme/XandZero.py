def check_game_over(game_state):
    game_ended = False
    winner = ''
    if ' ' not in game_state:
        winner = 'd'
        game_ended = True
        return game_ended, winner
    for i in [0, 3, 6]:
        if game_state[i] == game_state[i + 1] == game_state[i + 2] != ' ':
            game_ended = True
            return game_ended, game_state[i]
    for i in [0, 1, 2]:
        if game_state[i] == game_state[i + 3] == game_state[i + 6] != ' ':
            game_ended = True
            return game_ended, game_state[i]
    if game_state[0] == game_state[4] == game_state [8] != ' ':
        game_ended = True
        return game_ended, game_state[0]
    if game_state[2] == game_state[4] == game_state[6] != ' ':
        game_ended = True
        return game_ended, game_state[2]
    return game_ended, winner

def pick_computer_move(game_state):
    choice_order = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for i in choice_order:
        if game_state[i] == ' ':
            game_state[i] = 'o'
            # print('Computerul a ales pozitia: ', i + 1)
            return game_state
    return game_state

def pretty_print(game_state):
    for i in [0, 3, 6]:
        print(game_state[i] + ' | ' + game_state[i+1] + ' | ' + game_state[i+2])

if __name__ == '__main__':
    game_state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    possible_input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    game_ended = False
    winner = ''
    while game_ended != True:
        user_letter = int(input("Alege o cifra (1-9): ")) #TODO: verificare input pentru litere
        if user_letter not in possible_input:
            print('Nu ai ales o cifra valida, alege din nou!')
            continue
        if game_state[user_letter - 1] == ' ':
            game_state[user_letter - 1] = 'x'
            game_ended, winner = check_game_over(game_state)
            game_state = pick_computer_move(game_state)
            game_ended, winner = check_game_over(game_state)
        else:
            print('Pozitia nu este libera')
        pretty_print(game_state)
    if winner == 'x':
        print('GAME ENDED: You won')
    elif winner == 'o':
        print('GAME ENDED: Computer won')
    else:
        print('GAME ENDED: Draw')