def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        elif len(answer) == 0:
            answer.append(-1)

    return sorted(answer)
    #rwed
    #gds
