t = int(input())
def pr(n):
    if n < 2:
        return 'Not prime'
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

teks = ''
for i in range(t):
    n = int(input())
    teks += pr(n) + '\n'

print(teks)