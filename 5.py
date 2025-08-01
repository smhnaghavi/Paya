import sys

ans = 0
while True:
    ch = sys.stdin.read(1)
    if ch != '\n':
        ans ^= ord(ch)
    else: 
        break
while True:
    ch = sys.stdin.read(1)
    if ch != '\n':
        ans ^= ord(ch)
    else: 
        break



print(f"Extra character: {chr(ans)}")
