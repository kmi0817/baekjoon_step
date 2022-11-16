def solution(n, lost, reserve):
    std = [1] * (n+1) # 도난 당하기 전 상태
    for n in lost : # 도난 당한 학생
        std[n] -= 1
    for n in reserve : # 여벌 체육복 소유 학생
        std[n] += 1
    # 0 : 체육복 없음, 1 : 여벌 체육복X, 2 : 여벌 체육복O
    
    for i in range(1, n+2) :
        if i == 1 and std[i] == 0 and std[i+1] == 2 :
            std[i], std[i+1] = 1, 1
            
        elif i == (n+1) and std[i] == 0 and std[i-1] == 2 :
            std[i-1], std[i] = 1, 1
            
        else :
            if std[i] == 0 and std[i-1] == 2 :
                std[i-1], std[i] = 1, 1
            elif std[i] == 0 and std[i+1] == 2 :
                std[i], std[i+1] = 1, 1            
            
    answer = len(std[1:]) - std[1:].count(0)
    return answer