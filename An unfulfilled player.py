def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a in range(len(completion)):
        if participant[a] != completion[a]:
            answer = participant[a]
            break
        if not a:
            answer = participant[len(participant)-1]

            return answer
#refsd
