import time
start_time = time.time()
import uf
import math
from queue import Queue

lines = uf.read_lines("../in/20.in")[:-1]
tests = uf.read_lines("../test/20-2.in")[:-1]

#Flip-Flops tar bara korta pulser, stoppar alltid på långa pulser


def parse(puzzle):
    conj = []
    configuration = {}
    for line in puzzle:
        tn, modules = line.split(" -> ")
        t, name = tn[0], tn[1:]
        if t == "&":
            conj.append(name)
        modules = [module for module in modules.split(", ")]
        if t == "%":
            modules = (modules, False)
        configuration[name] = (t,modules)
    
    conjunctions = {}
    for c in conj:
        conjunctions[c] = []
        for line in puzzle:
            tn, modules = line.split(" -> ")
            t, name = tn[0], tn[1:]
            modules = [module for module in modules.split(", ")]
            if c in modules:
                conjunctions[c].append(name)

    for key in conjunctions.keys():
        l = conjunctions[key]
        conjunctions[key] = {k: False for k in l}
    return configuration, conjunctions

def p1(puzzle):
    config, conjun = parse(puzzle)
    high = 0
    low = 0
    rx = 0
    for i in range(1000):
        rx = 0
        q = Queue()
        q.put((0, "", "roadcaster")) 
        low += 1
        while not q.empty():
            pulse, sender, name = q.get() 
            if name == "rx":
                rx += 1
                continue
            t, modules = config[name]
            
        
            if t == "b":
                for module in modules:
                    q.put((0, name,  module))
                    low += 1

            elif t == "%" and pulse == 0:
                modules, on = modules
                mods = modules
                modules = modules, not on
                config[name] = t, modules
                if not on:
                    for module in mods:
                        q.put((1, name, module))
                        high += 1
                if on:
                    for module in mods:
                        q.put((0, name, module))
                        low += 1
                

            elif t == "&":
                if pulse == 0:
                    conjun[name][sender] = False
                elif pulse == 1:
                    conjun[name][sender] = True

                if all(conjun[name].values()):
                    for module in modules:
                        q.put((0, name, module))
                        low += 1
                else:
                    for module in modules:
                        q.put((1, name, module))
                        high += 1
    return high * low

def p2(puzzle):
    config, conjun = parse(puzzle) 
    cycles = []
    for i in range(1,10000): #Assuming cycles exist within the first 10000, attempts
        ks = 0
        pm = 0
        dl = 0
        vk = 0
        q = Queue()
        q.put((0, "", "roadcaster")) 
        while not q.empty():
            pulse, sender, name = q.get() 
            if name == "rx":
                continue
            t, modules = config[name]
            
        
            if t == "b":
                for module in modules:
                    q.put((0, name,  module))

            elif t == "%" and pulse == 0:
                modules, on = modules
                mods = modules
                modules = modules, not on
                config[name] = t, modules
                if not on:
                    for module in mods:
                        q.put((1, name, module))
                if on:
                    for module in mods:
                        q.put((0, name, module))
                

            elif t == "&":
                if pulse == 0:
                    conjun[name][sender] = False
                elif pulse == 1:
                    conjun[name][sender] = True

                if all(conjun[name].values()):
                    for module in modules:
                        q.put((0, name, module))
                else:
                    if name == "ks":
                        ks += 1
                    if name == "pm":
                        pm += 1
                    if name == "dl":
                        dl += 1
                    if name == "vk":
                        vk += 1
                    for module in modules:
                        q.put((1, name, module))
        if ks == 1:
            cycles.append(i)
        if pm == 1:
            cycles.append(i)
        if dl == 1:
            cycles.append(i)
        if vk == 1:
            cycles.append(i)
        if len(cycles) == 4:
            return math.lcm(*cycles)

print(p1(lines))
print(p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))     


