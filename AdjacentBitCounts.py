
f0 = [[-1 for _ in range(101)] for _ in range(101)]
f1 = [[-1 for _ in range(101)] for _ in range(101)]


def f(n, k):
    return f_ending_in_0(n, k) + f_ending_in_1(n, k)


def f_ending_in_0(n, k):
    if n == 1:
        return k == 0

    if f0[n][k] == -1:
        f0[n][k] = f(n - 1, k)

    return f0[n][k]


def f_ending_in_1(n, k):
    if n == 1:
        return k == 0

    if f1[n][k] == -1:
        f1[n][k] = f_ending_in_0(n - 1, k) + f_ending_in_1(n - 1, k - 1)

    return f1[n][k]


tests = int(input())
for t in range(tests):
    x, n, k = map(int, input().split())
    print(t+1, f(n, k))



