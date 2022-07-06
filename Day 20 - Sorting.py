if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    b = sorted(a)
    swap = 0
    i = 0
    ind = len(a)
    while a != b:
        round_swap = 0
        for j in range(i, len(a)-1):
            if a[j] > a[j+1]:
                a.insert(j + 2, a[j])
                a.pop(j)
                swap += 1
                round_swap += 1
            else:
                break
        ind -= 1
        if round_swap == 0:
            i += 1

        if a != b and a[i:] == sorted(a[i:]):
            i = 0
        # else:
        #     i = 0
        print(a, i, ind)
    print('Array is sorted in {} swaps.'.format(swap))
    print('First Element: {}\nLast Element: {}'. format(a[0], a[-1]))


