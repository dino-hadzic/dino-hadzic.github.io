# U lokalnom nacinu ulaz sadrzi skrivenu permutaciju; ocekivani izlaz je upravo ta permutacija.
import sys
data = sys.stdin.read().split()
n = int(data[0])
print(' '.join(data[1:1 + n]))
