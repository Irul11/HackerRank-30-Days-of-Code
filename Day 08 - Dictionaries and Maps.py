n = int(input())
dic = {}

for _ in range(n):
    pb = input().split()
    name, phone = pb[0], (pb[1])
    if name in dic.keys():
        dic[name] += phone
    else:
        dic[name] = phone

# Makai EOF eror biar tau kalau nggk ada input lagi
teks = ''
while True:
    try :
        query = input()
        if query:
            if query in dic.keys():
                teks += query + '=' + (dic[query]) + '\n'
            else:
                teks += 'Not found' + '\n'

    except EOFError:
        break

print(teks)

