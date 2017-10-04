from copy import deepcopy

p1d = list()
p2d = list()
p1t = list()
p2t = list()

def laydown(size):
    #add cards to table
    for x in range(size-1):
        p1t.append([p1d.pop(0), False])
        p2t.append([p2d.pop(0), False])
    #flip top cards
    p1t.insert(0,[p1d.pop(0), False])
    p2t.insert(0,[p2d.pop(0), False])
    p1t[0][1] = True
    p2t[0][1] = True

def pickup(winner):
    wd = list()
    p1t.reverse()
    p2t.reverse()
    t1 = deepcopy(p1t)
    t2 = deepcopy(p2t)
    if winner == 2:
        tmp = deepcopy(t2)
        t2 = deepcopy(t1)
        t1 = deepcopy(tmp)
    while 0 != len(t1):
        #print(t1)
        #print(t2)
        for card in t1:
            wd.append(card[0])
            t1.pop(0)
            if card[1]:
                break
        for card in t2:
            wd.append(card[0])
            t2.pop(0)
            if card[1]:
                break
    p1t.clear()
    p2t.clear()
    return wd

#get p1 deck
tmp = input()
for t in tmp.split():
    p1d.append(int(t))
#get p2 deck
tmp = input()
for t in tmp.split():
    p2d.append(int(t))

while 0 != len(p1d) and 0 != len(p2d):
    #determine fight size
    print("p1d: " + str(p1d))
    print("p2d: " + str(p2d))
    p1dSize = len(p1d)
    p2dSize = len(p2d)
    if p1dSize >= 4 and p2dSize >= 4:
        laydown(4)
    elif p1dSize >= 3 and p2dSize >= 3:
        laydown(3)
    elif p1dSize >= 2 and p2dSize >= 2:
        laydown(2)
    else:
        laydown(1)
    print("p1t: " + str(p1t))
    print("p2t: " + str(p2t))
    if p1t[0][0] > p2t[0][0]:
        print("p1")
        for card in pickup(1):
            p1d.append(card)
    elif p1t[0][0] < p2t[0][0]:
        print("p2")
        for card in pickup(2):
            p2d.append(card)
    else:
        continue
    print()
else:
    if 0 == len(p1d) and 0 == len(p2d):
        print("tie")
    elif 0 == len(p2d):
        print(1)
    else:
        print(2)