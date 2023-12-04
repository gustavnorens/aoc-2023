import uf
import time
start_time = time.time()

input = uf.read_lines("../in/input4.txt")[:-1]

def p1(lines):
    res,_ = zip(*map(score, lines))
    return sum(res)

def score(game):
    game = game[10:]
    wins, scores = game.split("|")
    wins = wins.split()
    scores = scores.split()
    total = 0
    for s in scores:
        if s in wins:
            total += 1
    return int(2**(total-1)), total

def p2(cards):
    R = len(cards)
    dick = {key: 1 for key in range(0,R)}
    for r, card in enumerate(cards):
        res = score(card)[1]
        for i in range(1, res+1):
            dick[r+i] += dick[r]
    return sum(value for key, value in dick.items() if key <= R)

print(p1(input))
print(p2(input))

print("--- %s seconds ---" % (time.time() - start_time))
