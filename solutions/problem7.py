import time
start_time = time.time()
import uf


lines = uf.read_lines("../in/7.in")[:-1]
test = uf.read_lines("../test/7.in")[:-1]

def parse(lines):
    res = []
    for line in lines:
            res.append(line.split())
    return res

def p1(lines):
    parsed = parse(lines)
    total = 0
    for hand, score in parsed:
        print(hand, score)
    hands, nums = zip(*parsed)
    scores = score_hands(parsed)
    sort = sorted(scores)
    print(sort)
    for i, scores in enumerate(sort):
         _, _, _, number = scores
         total += (i + 1) * int(number)
    return total
    


def score_hands(parsed):
    scores = []
    for hand, num in parsed:
        counter = 0
        firstCard = None
        secondCard = None
        new_hand = hand.replace("J", "")
        jokers = len(hand) - len(new_hand)
        print(hand)
        print(new_hand)
        for i in range(0, len(new_hand)):
            if new_hand[i] in new_hand[i+1:]:
                if (firstCard == None):
                    counter += 1
                    firstCard = new_hand[i]
                elif (firstCard == new_hand[i] or secondCard == new_hand[i]):
                    counter += 2
                else:
                    counter += 1
                    secondCard = new_hand[i]
        acc = ""
        if counter != 0:
            counter = counter + 2 * jokers
        else:
            if jokers == 5:
                counter = 7
            elif jokers == 4:
                counter = 7
            elif jokers == 3:
                counter = 5
            elif jokers == 2:
                counter = 3
            elif jokers  == 1:
                counter = 1
        for card in hand:
            if card.isdigit():
                acc += card
            elif card == "A":
                acc += "E"
            elif card == "K":
                acc += "D"
            elif card == "Q":
                acc += "C"
            elif card == "J":
                acc += "1"
            elif card == "T":
                acc += "A"
        score = counter, int(acc, 16), hand, num
        scores.append(score)
    return scores

        
def p2(lines):
    return None


print(score_hands([("KKK54","353"), ("AAAA5","535")]))
print(p1(lines))
print(p1(test))

print("--- %s seconds ---" % (time.time() - start_time))

