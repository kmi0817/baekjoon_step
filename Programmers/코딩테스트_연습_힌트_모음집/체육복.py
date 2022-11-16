def solution(n, lost, reserve):
    n_lost = list(set(lost) - set(reserve))
    n_reserve = list(set(reserve) - set(lost))
    
    borrow = set()
    for x in n_lost :
        if x-1 in n_reserve :
            borrow.add(x)
            n_reserve.remove(x-1)
        elif x+1 in n_reserve :
            borrow.add(x)
            n_reserve.remove(x+1)
            
    answer = n - (len(n_lost) - len(borrow))
    return answer