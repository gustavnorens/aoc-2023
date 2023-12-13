import uf
import time
start_time = time.time()

games = uf.read_lines("../in/2.in")[:-1]

class Bag:
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0

    def add_red(self, red):
        if (red > self.red):
            self.red = red

    def add_blue(self, blue):
        if (blue > self.blue):
            self.blue = blue
        
    def add_green(self, green):
        if (green > self.green):
            self.green = green

    def possible(self):
        return not (self.red > 12 or self.green > 13 or self.blue > 14)
    
    def power(self):
        return self.red * self.blue * self.green


def score(s):
    colon = s.find(":")
    game = int(s[4:colon])
    sets = s[colon+1:].split(";")

    bag = Bag()

    for set in sets:
        add_colors(set, bag)

    if bag.possible():
        return game, bag.power()
    return 0, bag.power()


def add_colors(set, bag):
    set = set.split(",")
    for elem in map(str.strip, set):
        add_color(elem, bag)

def add_color(elem, bag):
    num, color = elem.split(" ")
    num = int(num)
    if "blue" == color:
        bag.add_blue(num)
    if "red" == color:
        bag.add_red(num)
    if "green" == color:
        bag.add_green(num)


(fst, snd) = map(sum,zip(*list(map(score, games))))


print(fst)
print(snd)
print("--- %s seconds ---" % (time.time() - start_time))
    
