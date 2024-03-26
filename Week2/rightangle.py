s1 = int(input('Enter the length of the first side'))
s2 = int(input('Enter the length of the second side'))
s3 = int(input('Enter the length of the third side'))
hyp = 0
if s1 > s2:
    if s1 > s3:
        hyp = s1
elif s2 > s3:
    hyp = s2
else:
    hyp = s3
if hyp == s1:
    if s2 ** 2 + s3 ** 2 == hyp ** 2:
        print('It is a Right triangle')
    else:
        print('Not a right triangle')
elif hyp == s2:
    if s1 ** 2 + s3 ** 2 == hyp ** 2:
        print('It is a Right triangle')
    else:
        print('Not a right triangle')
else:
    if s1 ** 2 + s2 ** 2 == hyp ** 2:
        print('It is a Right triangle')
    else:
        print('Not a right triangle')