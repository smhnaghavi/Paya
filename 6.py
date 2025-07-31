def divide(a, b):
    ans = 0

    while a >= b:
        tmp = b
        d = 1
        while (tmp << 1) <= a:
            tmp <<= 1
            d <<= 1
        a -= tmp
        ans |= d

    return ans

a, b = map(int, input().split())
print(divide(a, b))
