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
former_max = -1
former_rank = -1
for rank in range(1, n+1) :
  max_elements = max(votes)
  max_index = votes.index(max_elements)

  if max_elements == former_max :
    ranks[max_index] = former_rank
  else :
    ranks[max_index] = rank
  former_max = max_elements
  former_rank = max_index

print(f"ranks: {ranks}")