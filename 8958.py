n = int(input())
for i in range(0, n):
    ox = input()
    plus = 0
    base = 1
    sum = 0

    for j in ox:
        if j == 'O':
            sum = sum + plus + base
            plus += 1
        else:
            plus = 0
    print(sum)