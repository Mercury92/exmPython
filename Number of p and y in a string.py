def solution(s):
    answer = True
    if(s.count('P') + s.count('p') != s.count('Y') + s.count('y')):
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
