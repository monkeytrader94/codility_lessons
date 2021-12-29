def solution(A):
    from collections import Counter

    N = len(A)
    if N == 0:
        return -1

    mode_and_frequency = Counter(A).most_common(1)[0]
    mode = mode_and_frequency[0]
    frequency = mode_and_frequency[1]

    if frequency <= N / 2:
        return -1
    else:
        for i in range(N):
            if A[i] == mode:
                return i
