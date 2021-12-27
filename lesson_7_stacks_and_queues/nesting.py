def solution(S):
    try:
        lst = []
        for char in S:
            if char == '(':
                lst.append(char)
            else:
                lst.pop()
                
        if lst != []:
            return 0
        
        return 1
        
    except:
        return 0
