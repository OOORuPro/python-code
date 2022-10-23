def solution(str):
    resString = ''
    for i in range(len(str)-1,-1,-1):
        resString+=str[i]
    return resString

print(solution("world"))