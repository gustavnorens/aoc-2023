import uf


input = uf.read_lines("input1.txt")[:-1]


numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

dick = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def lastFirst(s):
    s = ''.join(filter(str.isdigit,s))
    return int(s[0]+s[len(s)-1])

def find(s):
    lowest = 1000000000000000000000000
    highest = s.find(numbers[0])
    lowestNum = numbers[0]
    highestNum = numbers[0]
    for elem in numbers:
        if s.find(elem) < lowest and s.find(elem) >= 0:
            lowest = s.find(elem)
            lowestNum = elem
        if s.rfind(elem) > highest:
            highest = s.rfind(elem)
            highestNum = elem
    return (lowest, lowestNum, highest, highestNum)

def replace_them(s):
    (l,ln,h,hn) = find(s)
    r = s[:l]+repl(numbers,ln) + s[l+len(ln):h] 
    t = repl(numbers, hn) + s[h+len(hn):]
    s = r + t
    return s

def repl(strings, r):
    for s in strings:
        r = r.replace(s,dick[s])
    return r

output = list(map(replace_them, input))
print(output)
output = list(map(lastFirst, output))
print(sum(output))


sam = uf.read_lines("dumpy.txt")[:-1]

sam = list(map(int,sam))


def nice(input):
    sum = 0
    for s in input:
        digits = []
        for i,c in enumerate(s):
            if c.isdigit():
                digits.append(c)
            for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if s[i:].startswith(val):
                    digits.append(str(d+1))
        sum += int(digits[0]+digits[-1])
    return sum

def compare(l1, l2):
    for i in range(1000):
        if (l1[i] != l2[i]):
            return i
    return -1
