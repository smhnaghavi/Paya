def find_extra_char(s1, s2):
    result = 0
    for ch in s1:
        result ^= ord(ch)
    for ch in s2:
        result ^= ord(ch)
    return chr(result)

# دریافت ورودی از کاربر
s1 = input("رشته اول را وارد کنید: ")
s2 = input("رشته دوم را وارد کنید: ")

# پیدا کردن حرف اضافی
extra_char = find_extra_char(s1, s2)
print("حرف اضافی:", extra_char)
