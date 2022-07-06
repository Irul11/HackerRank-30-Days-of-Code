def review(s):
    even, odd = s[::2], s[1::2]
    print(even, odd)

for _ in range(int(input())):
    review(input())
