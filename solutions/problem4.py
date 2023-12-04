import uf
import time
start_time = time.time()
input = uf.read_lines("../in/input4.txt")[:-1]
test = uf.read_lines("../test/test4.txt")[:-1]
def p1(lines):
    res = map(score, lines)
    return sum(res)


def score(game):
    game = game[10:]
    wins, scores = game.split("|")
    wins = wins.split()
    scores = scores.split()
    total = 0
    for s in scores:
        if s in wins:
            if total == 0:
                total += 1
            else:
                total *= 2
    return total

def score2(game):
    game = game[10:]
    wins, scores = game.split("|")
    wins = wins.split()
    scores = scores.split()
    total = 0
    for s in scores:
        if s in wins:
            total += 1
    return total

def countGames(cards):
    R = len(cards)
    dick = {key: 1 for key in range(0,R)}
    for r, card in enumerate(cards):
        res = score2(card)
        for i in range(1, res+1):
            dick[r+i] += dick[r]
    return sum(value for key, value in dick.items() if key <= R)



print(p1(input))
print(countGames(input))

print("--- %s seconds ---" % (time.time() - start_time))
