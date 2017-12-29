

def zeros(n):
    power_of_five = 5

    acc = 0
    while power_of_five <= n:
        acc = acc + (n // power_of_five)
        power_of_five = power_of_five * 5

    return acc


testCases = int(input())

for case in range(testCases):
    print(zeros(int(input())))

