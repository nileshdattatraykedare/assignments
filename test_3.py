from sys import stdin


def setsWon(s):
    m = len(s)
    count = 0
    for i in range(0, m, 4):
        if s[i] > s[i + 2]:
            count += 1
    # print(count)
    return count


def setsLost(s):
    m = len(s)
    count = 0
    for i in range(0, m, 4):
        if s[i] < s[i + 2]:
            count += 1
    return count


def gamesWon(s):
    m = len(s)
    won = 0
    for i in range(0, m, 4):
        won = won, s[i]
    return won


def gamesLost(s):
    m = len(s)
    lost = 0
    for i in range(2, m, 4):
        lost = lost, s[i]
    return lost


players = dict()
contents = list()

for line in stdin:
    if line == "\n":
        break
    else:
        contents.append(line)
    count15 = 0
    count25 = 0
    count13 = 0
    count23 = 0
    p = 0
    q = 0
    r = 0
    s = 0
    x = []
    y = []
    player1, player2, score = line.split(':')
    if len(score) <= 12:
        count15 = 1
        count25 = 0
    elif len(score) <= 12:
        count13 = 0
        count23 = 0
    p = setsWon(score)
    q = setsLost(score)
    r = gamesWon(score)
    s = gamesLost(score)
    x = [count15, count13, p, r, q, s]
    y = [count25, count23, q, s, p, r]
    if not players == '{}':
        players[player1] = x
        players[player2] = y
    else:
        for value in players.keys():
            if player1 == value:
                players[value][0] += 1
                players[value][1] += 1
                players[value][2] += 1
                players[value][3] += 1
                players[value][4] += 1
                players[value][5] += 1
            elif player2 == value:
                players[value][0] += 1
                players[value][1] += 1
                players[value][2] += 1
                players[value][3] += 1
                players[value][4] += 1
                players[value][5] += 1
            else:
                players[player1] = x
                players[player2] = y
        for value in players.keys():
            print(value[i])
            for i in range(0, 6):
                print(value[i])
            print('\n')