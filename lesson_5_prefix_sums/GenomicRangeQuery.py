def solution(S, P, Q):

    ans = []

    for i in range(len(P)):
        list = S[P[i] : Q[i] + 1]
        if 'A' in list:
            ans.append(1)
        elif 'C' in list:
            ans.append(2)
        elif 'G' in list:
            ans.append(3)
        else:
            ans.append(4)

    return ans