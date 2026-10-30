# --8<-- [start:mul]
def mulPowerOfTwo(n, m):  # računa n*(2^m)
    return n << m


def divPowerOfTwo(n, m):  # računa n/(2^m)
    return n >> m


# --8<-- [end:mul]
# --8<-- [start:abs]
def Abs(n):
    return (n ^ (n >> 31)) - (n >> 31)
    """
    n>>31 daje predznak broja n: ako je n pozitivan, n>>31 je 0, ako je n negativan, n>>31 je -1
    ako je n pozitivan, n^0=n i broj se ne mijenja; ako je n negativan, imamo n^(-1)
    treba izračunati dvojni komplement brojeva n i -1 pa ih povezati operacijom XOR,
    rezultat je n s promijenjenim predznakom, jednak apsolutnoj vrijednosti n umanjenoj za 1; oduzimanjem -1 dobiva se apsolutna vrijednost
    """


# --8<-- [end:abs]
# --8<-- [start:minmax]
# ako je a >= b, (a - b) >> 31 je 0, inače je -1
def max(a, b):
    return b & ((a - b) >> 31) | a & (~(a - b) >> 31)


def min(a, b):
    return a & ((a - b) >> 31) | b & (~(a - b) >> 31)


# --8<-- [end:minmax]
# --8<-- [start:sgn]
# slučaj s 0 je iznimka
def isSameSign(x, y):
    return (x ^ y) >= 0


# --8<-- [end:sgn]
# --8<-- [start:get_bit]
# dohvaća b-ti bit od a, najniži bit ima indeks 0
def getBit(a, b):
    return (a >> b) & 1


# --8<-- [end:get_bit]
# --8<-- [start:unset_bit]
# postavlja b-ti bit od a na 0, najniži bit ima indeks 0
def unsetBit(a, b):
    return a & ~(1 << b)


# --8<-- [end:unset_bit]
# --8<-- [start:set_bit]
# postavlja b-ti bit od a na 1, najniži bit ima indeks 0
def setBit(a, b):
    return a | (1 << b)


# --8<-- [end:set_bit]
# --8<-- [start:flap_bit]
# invertira b-ti bit od a, najniži bit ima indeks 0
def flapBit(a, b):
    return a ^ (1 << b)


# --8<-- [end:flap_bit]


if __name__ == "__main__":
    a, b = map(int, input().split())

    for i in range(16):
        print(f"{mulPowerOfTwo(a, i)} {divPowerOfTwo(a, i)}")

    assert Abs(-a) == a
    assert Abs(a) == a

    assert max(a, b) == (a if a > b else b)
    assert min(a, b) == (a if a < b else b)

    print(int(isSameSign(a, b)))

    for i in range(32):
        print(f"{getBit(a, i)} {unsetBit(a, i)} {setBit(a, i)} {flapBit(a, i)}")
