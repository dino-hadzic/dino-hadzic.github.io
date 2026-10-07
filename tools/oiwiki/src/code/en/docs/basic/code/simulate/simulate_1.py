u, d, n = map(int, input().split())
time = dist = 0
while True:  # Infinite loop to enumerate the steps
    dist += u
    time += 1
    if dist >= n:  # Leave the loop once the condition is met
        break
    dist -= d
print(time)  # Print the result
