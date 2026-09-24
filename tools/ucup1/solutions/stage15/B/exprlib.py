# Zajednicki pomocni kod za gen.py i check.py: stablo izraza, vrednovanje, parser po gramatici.
import math, random

class Los(Exception):
    pass

def evaluiraj(node, x, min_div):
    # node = ('x',) | ('sin', a) | ('cos', a) | ('+', a, b) ...
    t = node[0]
    if t == 'x':
        return x
    if t in ('sin', 'cos'):
        return getattr(math, t)(evaluiraj(node[1], x, min_div))
    a = evaluiraj(node[1], x, min_div); b = evaluiraj(node[2], x, min_div)
    if t == '+': return a + b
    if t == '-': return a - b
    if t == '*': return a * b
    if abs(b) < min_div:
        raise Los('dijeljenje s premalim nazivnikom')
    return a / b

def slozenost(node):
    t = node[0]
    if t == 'x': return 0
    if t in ('sin', 'cos'): return 1 + slozenost(node[1])
    return 2 + slozenost(node[1]) + slozenost(node[2])

def slucajno_stablo(c):
    # slucajno stablo tocno zadane slozenosti c
    if c == 0:
        return ('x',)
    izbori = []
    if c >= 1: izbori.append('u')
    if c >= 2: izbori.append('b')
    if random.choice(izbori) == 'u':
        return (random.choice(['sin', 'cos']), slucajno_stablo(c - 1))
    i = random.randint(0, c - 2)
    return (random.choice('+-*/'), slucajno_stablo(i), slucajno_stablo(c - 2 - i))

def u_tekst(node):
    t = node[0]
    if t == 'x': return 'x'
    if t in ('sin', 'cos'): return t + '(' + u_tekst(node[1]) + ')'
    a, b = u_tekst(node[1]), u_tekst(node[2])
    if node[1][0] in '+-*/': a = '(' + a + ')'
    if node[2][0] in '+-*/': b = '(' + b + ')'
    return a + t + b

def parsiraj(s):
    # rekurzivni spust: E -> T (('+'|'-') T)*,  T -> F (('*'|'/') F)*,  F -> x | sin(E) | cos(E) | (E)
    pos = [0]
    def peek():
        return s[pos[0]] if pos[0] < len(s) else ''
    def E():
        node = T()
        while peek() in ('+', '-'):
            op = s[pos[0]]; pos[0] += 1
            node = (op, node, T())
        return node
    def T():
        node = F()
        while peek() in ('*', '/'):
            op = s[pos[0]]; pos[0] += 1
            node = (op, node, F())
        return node
    def F():
        if s.startswith('x', pos[0]):
            pos[0] += 1; return ('x',)
        for fn in ('sin', 'cos'):
            if s.startswith(fn + '(', pos[0]):
                pos[0] += len(fn) + 1
                node = E()
                if peek() != ')': raise Los('ocekivana )')
                pos[0] += 1
                return (fn, node)
        if peek() == '(':
            pos[0] += 1
            node = E()
            if peek() != ')': raise Los('ocekivana )')
            pos[0] += 1
            return node
        raise Los('neocekivan znak na poziciji %d' % pos[0])
    node = E()
    if pos[0] != len(s):
        raise Los('visak znakova')
    return node
