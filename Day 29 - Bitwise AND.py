# Complete the 'bitwiseAnd' function below.

# Function for return a decimal number in biner
def biner(n):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

# Function for return a biner number in decimal
def decimal(n):
    n = n[::-1]
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * 2**i
    return result

# Function to get biner number with AND operation between a and b
def comp(a,b):
    result = ''
    for i in range(len(a)):
        if b[i] == a[i]:
            result += b[i]
        else:
            result += '0'
    return result

# Function to get maximum possible value that less than K
def bitwiseAnd(N, K):
    # maks is the initital maximum possible value
    maks = K - 1
    maks2bin = biner(maks)

    ### Conditional statement for N == 1
    if N == 1:
        return 0

    ### Conditional statement for N > 1
    # If maks less than N and an even number,
    # we can get maks as the maximum possible value
    if maks < N and maks % 2 == 0:
        return maks

    # If maks less than N and an odd number, we should to do something with maks to ensure
    # that maks is the maximum possible value
    if maks < N and maks % 2 != 0:
        # if we assume a = maks and b = int(i) for i in range(a + 2, N + 1, 2)
        # then if we get a AND b equal to maks, so we can get maks to be the maximum possible value
        for i in range(maks+2, N+1, 2):
            c = biner(maks)
            b = biner(i)
            a = '0'*(len(b) - len(c)) + c
            comp_result = decimal(comp(a,b))
            if comp_result == maks:
                return maks
        # Use recursion if maks is not able to be maximum possible value
        else:
            return bitwiseAnd(N-1, K)

    # If maks bigger or equal than N, we can assume that maximum -
    # possible value is N-1 if N - 1 is an even number.
    # IF N-1 is an odd number, we can use recursion to make N-1 finally an even number
    if maks >= N:
        if (N - 1) % 2 == 0:
            return N-1
        else:
            return bitwiseAnd(N-1, K)


t = int(input().strip())
for _ in range(t):
    first_multiple_input = input().rstrip().split()
    count = int(first_multiple_input[0])
    lim = int(first_multiple_input[1])
    res = bitwiseAnd(count, lim)
    print(res)





