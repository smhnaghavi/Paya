def divide(a, b):
    ans = 0
    tmp = b
    cnt = 1
    while (tmp << 1) <= a:
        tmp <<= 1
        cnt <<= 1
    while tmp >= b:
        if a >= tmp:
            a -= tmp
            ans += cnt
        tmp >>= 1
        cnt >>= 1
    return ans

a, b = map(int, input("Enter 2 numbers a & b: ").split())
print(divide(a, b))
