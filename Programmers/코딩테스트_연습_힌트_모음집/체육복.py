def solution(n, lost, reserve):
    std = [1] * (n+1) # 도난 당하기 전 상태
    for n in lost : # 도난 당한 학생
        std[n] -= 1
    for n in reserve : # 여벌 체육복 소유 학생
        std[n] += 1
    # 0 : 체육복 없음, 1 : 여벌 체육복X, 2 : 여벌 체육복O
    print(std)
    
    for index, value in enumerate(std[:n]) :
        if index == 0 : continue # 인덱스 0은 건너뜀
        
        if value == 0 and std[index+1] == 2 : # 뒷사람이 앞사람한테 빌려줌
            std[index], std[index+1] = 1, 1
            
    answer = len(std[1:]) - std[1:].count(0)
    return answer