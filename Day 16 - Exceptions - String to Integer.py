S = input()
try:
    print(int(S))
except ValueError as a:
    a = 'Bad String'
    print(a)