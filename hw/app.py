def hailstone(n):
    count = 1
    while n != 1:
        print(n)
        count += 1

        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    return count

print('count ', hailstone(50))