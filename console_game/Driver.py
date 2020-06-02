'''
Game Matters
'''

playerTurn = 1  # init turns
totalMoves = 0  # counting the turns
winner = 0

p1 = input('Enter the name of player #1: ')
p2 = input('Enter the name of player #2: ')

game = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' ',
}

def checkWinner():

    '''
     Case: Player 1
     '''

    # Horizontal
    if game['A1'] == 'X' and game['A2'] == 'X' and game['A3'] == 'X':
        print(f'{p1} is the a winner')
        return 1
    if game['B1'] == 'X' and game['B2'] == 'X' and game['B3'] == 'X':
        print(f'{p1} is the a winner')
        return 1
    if game['C1'] == 'X' and game['C2'] == 'X' and game['C3'] == 'X':
        print(f'{p1} is the a winner')
        return 1

    # Diagonal
    if game['A1'] == 'X' and game['B2'] == 'X' and game['C3'] == 'X':
        print(f'{p1} is the a winner')
        return 1

    if game['A3'] == 'X' and game['B2'] == 'X' and game['C1'] == 'X':
        print(f'{p1} is the a winner')
        return 1

     # Vertical Check
    if game['A1'] == 'X' and game['B1'] == 'X' and game['C1'] == 'X':
        print(f'{p1} is the a winner')
        return 1
    if game['A2'] == 'X' and game['B2'] == 'X' and game['C2'] == 'X':
        print(f'{p1} is the a winner')
        return 1
    if game['A3'] == 'X' and game['B3'] == 'X' and game['C3'] == 'X':
        print(f'{p1} is the a winner')
        return 1

    '''
    Case: Player 2
    '''

    # Horizontal
    if game['A1'] == 'O' and game['A2'] == 'O' and game['A3'] == 'O':
        print(f'{p2} is the a winner')
        return 1
    if game['B1'] == 'O' and game['B2'] == 'O' and game['B3'] == 'O':
        print(f'{p2} is the a winner')
        return 1
    if game['C1'] == 'O' and game['C2'] == 'O' and game['C3'] == 'O':
        print(f'{p2} is the a winner')
        return 1

    # Diagonal
    if game['A1'] == 'O' and game['B2'] == 'O' and game['C3'] == 'O':
        print(f'{p2} is the a winner')
        return 1

    if game['A3'] == 'O' and game['B2'] == 'O' and game['C1'] == 'O':
        print(f'{p2} is the a winner')
        return 1

     # Vertical Check
    if game['A1'] == 'O' and game['B1'] == 'O' and game['C1'] == 'O':
        print(f'{p2} is the a winner')
        return 1
    if game['A2'] == 'O' and game['B2'] == 'O' and game['C2'] == 'O':
        print(f'{p2} is the a winner')
        return 1
    if game['A3'] == 'O' and game['B3'] == 'O' and game['C3'] == 'O':
        print(f'{p2} is the a winner')
        return 1

    return 0

print()
print()
print('A1|A2|A3')
print('- +- +-')
print('B1|B2|B3')
print('- +- +-')
print('C1|C2|C3')
print('- +- +-')
print()

while True:
    print(game['A1'] + '|' + game['A2'] + '|' + game['A3'])
    print('-+-+-')
    print(game['B1'] + '|' + game['B2'] + '|' + game['B3'])
    print('-+-+-')
    print(game['C1'] + '|' + game['C2'] + '|' + game['C3'])
    winner = checkWinner()

    if totalMoves == 9 or winner == 1:  # game ends
        break

    while True:
        if playerTurn == 1:
            print()
            p1_input = input(f'{p1}, enter the position: ').upper()

            if p1_input in game and game[p1_input] == ' ':
                game[p1_input] = 'X'
                playerTurn = 2
                break
            else:
                print('Invalid input. Try again')
                continue
        else:
            print()
            p2_input = input(f'{p2}, enter the position: ').upper()

            if p2_input in game and game[p2_input] == ' ':
                game[p2_input] = 'O'
                playerTurn = 1
                break
            else:
                print('Invalid input. Try again')
                continue
    totalMoves += 1
