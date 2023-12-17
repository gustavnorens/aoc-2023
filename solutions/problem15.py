import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/14.in")[:-1]
tests = uf.read_lines("../test/14.in")[:-1]

with open ("../in/15.in", "r") as file:
    file = file.read().replace("\n", "")
    content = file.split(",")

def hash(word):
    product = 0
    for i in word.encode():
        product += i
        product *= 17
        product = product % 256
    return product


def parsing(words):
    dict = {}
    for word in words:
        if word[-1] == "-":
            key = hash(word[:-1])
            if key not in dict.keys():
                dict[key] = []
            for val in dict[key]:
                if word[:-1] == val[:-2]:
                    dict[key].remove(val)
        else:
            key = hash(word[:-2])
            if key not in dict.keys():
                dict[key] = [word[:-2] + " " + word[-1]]
            else:
                for i, val in enumerate(dict[key]):
                    if word[:-2] == val[:-2]:
                        dict[key][i] = val[:-1] + word[-1]
                        break
                else:
                    dict[key].append(word[:-2] + " " + word[-1])
    return dict

d = parsing(content)

print(sum(map(hash,content)))
total = 0
for i in range(256):
    if i in d.keys():
        for j, elem in enumerate(d[i]):
            res = (i + 1) * (j+1) * int(elem[-1])
            total += res
print(total)

print("--- %s seconds ---" % (time.time() - start_time))