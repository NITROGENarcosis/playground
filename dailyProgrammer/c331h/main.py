#from sys import stdin
#import re

def tokenize(line):
    a = line.rfind('(')
    b = line.rfind(')')
    c = line.rfind('^')
    d = line.rfind('/')
    e = line.rfind('*')
    f = line.rfind('-')
    g = line.rfind('+')
    h = line.rfind('=')
    m = max(a,b,c,d,e,f,g,h)
    if -1 == m :
        parts = []
        parts.append(line)
        #print(parts)
        return parts
    else:
        parts = []
        parts.append(line[m])
        parts.append(line[m+1:])
        #print(parts)
        #print(line[:m])
        nparts = tokenize(line[:m])
        for part in parts:
            nparts.append(part)
        #nparts.append(parts)
        while '' in nparts:
            nparts.remove('')
        return nparts


def pres(a, b):
    presRef = { '^': 4, '/': 3, '*': 3, '+': 2, '-': 2, '(':1, '`': 5 }
    if(presRef[a] <= presRef[b]):
        return True
    else:
        return False


def parseToPostFix(line):
    lineParts = tokenize(line)
    for x in range(len(lineParts)):
        if lineParts[x] == '-':
            if x == 0:
                lineParts[x] = '`'
            elif lineParts[x-1] in '/*-+()':
                lineParts[x] = '`'
    #print(lineParts)
    outQ = []
    opS = []
    for t in lineParts:
        #print(t)
        #print(outQ)
        #print(opS)
        #print(' ')
        if t not in "()/*-+^`":
            if t in vars:
                outQ.append(str(vars[t]))
            else:
                outQ.append(t)
        if t in "/*-+^`":
            while len(opS)>0:
                #if opS[0] == '^':
                   # break
                if pres(t,opS[0]) :
                    outQ.append(opS.pop(0))
                else:
                    break
            opS.insert(0, t)
        if t == '(':
            opS.insert(0, t)
        if t == ')':
            #print(opS)
            if len(opS)>0:
                while opS[0] != '(':
                    #print(opS)
                    outQ.append(opS.pop(0))
                    if not len(opS)>0:
                        break
                opS.pop(0)
    for t in opS:
        outQ.append(t)
    #print(outQ)
    return outQ


def parsePostToValue(line):
    stack = []
    for t in line:
        if t in '/*-+^':
            op2 = float(stack.pop(0))
            op1 = float(stack.pop(0))
            res = 0.0
            if t == '/':
                res = op1 / op2
            elif t == '*':
                res = op1 * op2
            elif t == '+':
                res = op1 + op2
            elif t == '-':
                res = op1 - op2
            elif t == '^':
                res = op1 ** op2
            else:
                exit(1)
            stack.insert(0, res)
        elif t == '`':
            op1 = float(stack.pop(0))
            res = op1 * -1.0
            stack.insert(0, res)
        else:
            stack.insert(0, t)
    return stack.pop(0)


vars = dict()

while True:
    newVar=False
    try:
        line = input()
    except:
        exit()
    if line.find('=') != -1:
        newVar = True
        var, line = line.split('=')
    postFline = parseToPostFix(line)
    val = parsePostToValue(postFline)
    if newVar:
        vars[var]=val
    print(val)
    print(vars)


