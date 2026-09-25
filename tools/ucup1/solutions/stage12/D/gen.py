import sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
if mode == 'big':
    print([1000, 999, 998, 997, 996, 995][(seed - 1) % 6])
else:
    print(17 + (seed - 1) % 984)  # svi N iz [17,1000]
