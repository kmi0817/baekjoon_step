n = int(input())
data = list()
for i in range(n) :
  kg, cm = map(int, input().split())
  data.append([kg, cm])

votes = [ 0 for i in range(n)]
for i, x in enumerate(data) :
  for y in data[i+1:] :
    if x[0] >= y[0] and x[1] >= y[1] :
      votes[i] += 1

ranks = [ 0 for i in range(n)]
former_max_value = -1
former_rank = -1
for i in range(1, n+1) :
  max_value = max(votes)

  if max_value == former_max_value :
    ranks[votes.index(max_value)] = former_rank
  else :
    ranks[votes.index(max_value)] = i
    former_max_value = max_value
    former_rank = i
    
  votes[votes.index(max_value)] = -1

    
for i, rank in enumerate(ranks) :
  if i == len(ranks) - 1 :
    print(rank)
  else :
    print(rank, end=" ")