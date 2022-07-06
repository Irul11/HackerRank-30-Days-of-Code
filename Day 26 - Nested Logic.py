# Enter your code here. Read input from STDIN. Print output to STDOUT
ret = list(map(int, input().split()))
due = list(map(int, input().split()))


def library(ret, due):
    # Tahun pengembalian lebih kecil
    if ret[2] < due[2]:
        return 0
    #  Tahun pengembalian sama
    elif ret[2] == due[2]:
        # Bulan pengembalian lebih kecil
        if ret[1] < due[1]:
            return 0
        # Bulan pengembalian sama
        elif ret[1] == due[1]:
            if ret[0] <= due[0]:
                return 0
            else:
                return 15 * (ret[0] - due[0])
        # Bulan pengembalian lebih 
        else:
            return 500 * (ret[1] - due[1])
    else:
        return 10000

print(library(ret, due))