u, d, n = map(int, input().split())
time = dist = 0
while True:  # Beskonačna petlja za nabrajanje koraka
    dist += u
    time += 1
    if dist >= n:  # Kad je uvjet ispunjen, izađi iz petlje
        break
    dist -= d
print(time)  # Ispiši rezultat
