# 06-11-2022

if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')
