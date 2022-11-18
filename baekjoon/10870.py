def recursive(k) :
  if k < 2:
    return k

  return recursive(k-1) + recursive(k-2)
  
n = int(input())

answer = recursive(n)
print(answer)
