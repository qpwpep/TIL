A, B, C = map(int, input().split())
def mod_pow(a, b, m):
    res = 1
    a %= m
    while b:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res
print(mod_pow(A, B, C))
