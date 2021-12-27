def solution(A):

    A.sort()
    if A[-1] == 0 or A[-2] == 0 or A[-3] == 0:
        return max([A[-1] * A[-2] * A[-3], 0, A[0] * A[1] * A[-1]])
    else:
        return max([A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1]])