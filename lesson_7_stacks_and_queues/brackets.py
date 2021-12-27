def solution(S):
    try:
        lst = []
        for char in S:
            if char == '(' or char == '[' or char == '{':
                lst.append(char)
            elif char == ')':
                if lst.pop() != '(':
                    return 0

            elif char == ']':
                if lst.pop() != '[':
                    return 0

            elif char == '}':
                if lst.pop() != '{':
                    return 0
        
        if lst != []:
            return 0
        
        return 1
        
    except:
        return 0