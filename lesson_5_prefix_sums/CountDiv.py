def solution(A, B, K):

    highest = B - (B % K)
    if A % K != 0:
        lowest = A + K - (A % K)
    else:
        lowest = A

    return int((highest - lowest) / K) + 1