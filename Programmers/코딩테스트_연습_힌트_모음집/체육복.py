def solution(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for x in _reserve:
        if x-1 in _lost:
            _lost.remove(x-1)
        elif x+1 in _lost:
            _lost.remove(x+1)
    answer = n - len(_lost)
    return answer