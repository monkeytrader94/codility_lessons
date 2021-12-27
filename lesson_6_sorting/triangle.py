def solution(A):

    A.sort()
    lst_length = len(A)

    if lst_length >= 3:
        for i in range(lst_length - 2):
            P, Q, R = A[i], A[i+1], A[i+2]

            if (P + Q > R and
            Q + R > P and
            R + P > Q):
                return 1

    return 0