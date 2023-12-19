import time
start_time = time.time()
import uf
import copy

lines = uf.read_lines("../in/19.in")[:-1]
tests = uf.read_lines("../test/19.in")[:-1]

xmas = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}

def parse(puzzle):
    workflows = []
    rules = []
    wfs = True
    for line in puzzle:
        if line == "":
            wfs = False
            continue
        if wfs:
            workflows.append(line)
        else:
            rules.append(line)
    wfs = {}
    for workflow in workflows:
        name = workflow[:workflow.find("{")]
        _workflow = workflow[workflow.find("{")+1:-1]
        _wfs = [wf for wf in _workflow.split(",")]
        l = []
        for wf in _wfs[:-1]:
            rule, dest = wf.split(":")
            v = xmas[rule[0]]
            sign = rule[1]
            num = int(rule[2:])
            l.append((v, sign, num, dest))
        l.append(_wfs[-1])
        wfs[name] = l 
    rules = [parse_rule(rule) for rule in rules]
    return wfs, rules

def parse_rule(rule):
    res = []
    rule = rule[1:-1]
    for r in rule.split(","):
        res.append(int(r[2:]))
    return res

def accepted(rule, wfs):
    current = "in"
    while True:
        if current == "R" or current == "A":
                break
        _wfs = wfs[current]
        for r in _wfs[:-1]:
            i, sign, num, dst = r
            if sign == ">":
                if rule[i] > num:
                    current = dst
                    break
            elif sign == "<":
                if rule[i] < num:
                    current = dst
                    break
        else:
            current = _wfs[-1]
    if current == "R":
        return False
    elif current == "A":
        return True
    return None

def p1(puzzle):
    wfs, rules = parse(puzzle)
    total = 0
    for rule in rules:
        if accepted(rule, wfs):
            total += 1
    return total

def len_range(range):
    x,y = range
    return y-x+1

#Let's look at a smaller example

def calc_range(wfs):
    stack = []
    total = 0
    stack.append(("in", [(1,4000), (1,4000), (1,4000),(1,4000)]))
    while stack:
        current, ranges = stack.pop()
        if current == "R":
            continue 
        if current == "A":
            p = 1
            for range in ranges:
                p *= len_range(range)        
            total += p
            continue
        workflows = wfs[current]
        last = workflows[-1]
        for workflow in workflows[:-1]:
            i, sign, num, dst = workflow
            start, end = ranges[i] 
            if sign == ">":
                if num < start:
                    stack.append((dst, copy.deepcopy(ranges)))
                elif start <= num < end:
                    new_ranges = copy.deepcopy(ranges)
                    new_ranges[i] = num+1, end
                    stack.append((dst, new_ranges))
                    ranges[i] = start, num
            elif sign == "<":
                if end < num:
                    stack.append((dst, copy.deepcopy(ranges)))
                elif start < num <= end:
                    new_ranges = copy.deepcopy(ranges)
                    new_ranges[i] = start, num -1
                    stack.append((dst, new_ranges))
                    ranges[i] = num , end

        new_ranges = copy.deepcopy(ranges)
        stack.append((last ,new_ranges))
    return total

def p2(puzzle):
    wfs, _ = parse(puzzle)    
    return calc_range(wfs)
print(p1(lines))
print(p2(lines))
print("--- %s seconds ---" % (time.time() - start_time))     