def solution(s):
    a = len(s)

    if a % 2 == 0:
        answer = s[int(a/2-1)] + s[int(a/2)]
    else:
        answer = s[int(a // 2)]

    return answer
    #fsefd
