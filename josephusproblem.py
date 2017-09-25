# https://en.wikipedia.org/wiki/Josephus_problem
def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n-1, k) + k - 1) % n + 1

n = 100
k = 2
print('Josephus Problem: n={:d}, k={:d}'.format(n, k))
print('To be alive, start at position {:d}'.format(josephus(n, k)))

