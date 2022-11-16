def solution(n, lost, reserve):
    std = [1] * n # 도난 당하기 전 상태
    for i in lost : # 도난 당한 학생
        std[i-1] -= 1
    for i in reserve : # 여벌 체육복 소유 학생
        std[i-1] += 1
    # 0 : 체육복 없음, 1 : 여벌 체육복X, 2 : 여벌 체육복O
    
    for i in range(n) :
        if i > 0 :
            if std[i-1] == 0 and std[i] == 2 :
                std[i-1], std[i] = 1, 1
        
        if i < n-1 :
            if std[i] == 0 and std[i+1] == 2 :
                std[i], std[i+1] = 1, 1
            
    answer = len(std) - std.count(0)
    return answer