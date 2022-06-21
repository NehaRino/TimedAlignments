#this is how mixed moves operate when propogating backwards on a delay series
def delmove(s, d, i, l) : 
  if i > 0 : 
    l[i-1] = l[i-1] + s
  l[i] = l[i] - s + d

#mixed backward lines 
def mixbackward(og, os) : 
  g = og.copy()
  s = os.copy()

  g.insert(0, 0)
  s.insert(0,0)
  delg = []
  dels = []
  for i in range(len(g)-1): 
    delg.append(g[i+1] - g[i])
    dels.append(s[i+1] - s[i])
  cost = 0 
  stamp = 0 
  delay = 0
  i = len(dels)-1
  #print(i, cost, delg, dels)

  while i > 0 : 
    curr = delg[i] - dels[i]
    next = delg[i-1] - dels[i-1]
    if curr*next >= 0 : 
      delmove(0, curr, i, dels)
    elif abs(curr) < abs(next) : 
      delmove(-curr, 0, i, dels)
    else : 
      delmove(next, curr - next, i, dels)
    cost = cost + abs(curr)
    #print(i, cost, delg, dels)
    i = i-1
  cost = cost + abs(delg[i] - dels[i])
  return cost


##As a bonus, we include an implementation of the algorithm that works chronologically on the timing function representation

#This is how a mixed move works moving forward, on an actual time stamp series
def tracemove(s, d, i, l): 
  if i < len(l): 
    l[i] = l[i] + s
    while i < len(l) : 
      l[i] = l[i] + d
      i = i+1

#mixed forward lines 

def mixforward(og, os) : 
  s = os.copy()
  g = og.copy()
  cost = 0 
  stamp = 0 
  delay = 0
  i = 0
  #print(i , cost, g, s )
  while i < len(s)-1: 
    curr = g[i] - s[i]
    next = g[i+1] - s[i+1]
    if curr*next < 0: 
      tracemove(curr, 0, i, s)
    elif abs(next) < abs(curr) : 
      tracemove(curr-next, next, i, s)
    else: 
      tracemove(0, curr, i, s)
    cost = cost + abs(curr)
    #print(i , cost, g, s )
    i = i+1
  cost = cost + abs(g[i] - s[i])
  return cost

