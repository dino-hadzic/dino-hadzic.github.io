import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(2, 7); k = random.randint(2, n)
        alpha = random.choice(['ab', 'abc', 'abcd'])
        maxlen = random.choice([2, 3, 5])
        print(n, k)
        for i in range(n):
            L = random.randint(1, maxlen)
            print(''.join(random.choice(alpha) for _ in range(L)))
else:
    kind = random.randint(0, 2)
    print(1)
    if kind == 0:
        # mnogo kratkih nizova
        n = 500000; k = random.randint(2, n)
        print(n, k)
        print("\n".join(''.join(random.choice('ab') for _ in range(2)) for _ in range(n)))
    elif kind == 1:
        # jedan dugačak + par kratkih: dubok trie
        n = 3; k = 2
        print(n, k)
        print('a' * 999990)
        print('a' * 5 + 'b')
        print('b')
    else:
        # srednje: 10^4 nizova duljine 100 s zajedničkim prefiksima
        n = 10000; k = random.randint(2, n)
        print(n, k)
        pre = ''.join(random.choice('abc') for _ in range(50))
        print("\n".join(pre[:random.randint(0, 50)] + ''.join(random.choice('abcz') for _ in range(50)) for _ in range(n)))
