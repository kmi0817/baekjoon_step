# the book' solution using sorting

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k) :
  if a[i] > b[i] :
    break

  a[i], b[i] = b[i], a[i]

print(sum(a))


# my solution without sorting
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k) :
  min_a = min(a)
  max_b = max(b)

  if min_a >= max_b :
    break

  index_a = a.index(min_a)
  index_b = b.index(max_b)
  a[index_a] = max_b
  b[index_b] = min_a

print(sum(a))
