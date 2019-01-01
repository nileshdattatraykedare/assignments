def orangecap(a):
    b = {}
    for k1 in a:
        for k2 in a[k1]:
            b[k2] = b.get(k2, 0) + a[k1][k2]
    player = max(b, key=b.get)
    return {'playername': player, 'topscore': b[player]}


data = {'match1': {'player1': 57, 'player2': 38},
        'match2': {'player3': 9, 'player1': 42},
        'match3': {'player2': 41, 'player4': 63, 'player3': 91}}

print (orangecap(data))
# result {'playername': 'player3', 'topscore': 100}
