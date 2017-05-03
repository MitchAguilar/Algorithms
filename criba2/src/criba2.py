def criba_eratostenes(n):
  l=[]
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      l.append(i)
      multiplos.update(range(i*i, n+1, i))
  return l

print(criba_eratostenes(201000))
