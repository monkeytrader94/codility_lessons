def solution(H):

    count = 1
    stack = [H[0]]
    for i in range(1, len(H)):
        if H[i] > stack[-1]:
            stack.append(H[i])
            count += 1
        elif H[i] == stack[-1]:
            continue
        elif H[i] < stack[-1]:
            try:
                while H[i] < stack[-1]:
                    stack.pop()
            except IndexError:
                stack.append(H[i])
                count += 1
            if H[i] > stack[-1]:
                stack.append(H[i])
                count += 1
            elif H[i] == stack[-1]:
                continue

    return count
