def solution(A, B):

    ones = []
    living = 0

    for i in range(len(A)):
        if B[i] == 1:
            ones.append(A[i])
        else:
            if ones == []:
                living += 1
            else:
                try:
                    while A[i] > ones[-1]:
                        ones.pop()
                except IndexError:
                    living += 1

    living += len(ones)

    return living
