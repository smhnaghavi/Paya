def find_extra_char(s1, s2):
    result = 0
    for ch in s1:
        result ^= ord(ch)
    for ch in s2:
        result ^= ord(ch)
    return chr(result)
    
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

extra_char = find_extra_char(s1, s2)
print("Extra character:", extra_char)
