#somewhere to keep auxiliary functions useful for mainly stamp aligning

#this is a convenient binary search algorithm on the ylist graph construct
def binary(ylist, x) : 
  i = 0
  if(ylist == []): 
    return None
  h = len(ylist) -1
  if x < ylist[0][0] or x > ylist[h][1] :
    return None 
  else : 
    l = 0
    k = math.floor((h + l)/2)
    
    while l <= h : 
      i = i + 1
      if x >= ylist[k][0] and x < ylist[k][1] : 
        return k 
      elif x < ylist[k][0] : 
        h = k-1
      else : 
        l = k+1
      if i > 20 : 
        break
      k = math.floor((h + l)/2)

#implementing the backtracking function that given min cost pops out a process trace on which the minimum is realised. 
def backtrack(trace, graphlist, cost, net) : 
  i = 0
  ylist = []
  yfirst = 0
  gamma = []
  for i in range(len(graphlist)) : 
    j = 0
    yfirst = yfirst + abs(graphlist[i].segments[0][0] - trace[i])
    yright = yfirst 
    ylist.append([])
    for j in range(len(graphlist[i].segments)) :
      yleft = yright
      segment = graphlist[i].segments[j]
      yright = yleft + segment[1]*(segment[2] - segment[0])
      ylist[i].append([yleft, yright])

  i = len(trace) - 1
  gamma = [0]*len(trace)
  while(i > -1): 
    nadir = 0
    if i+1 < len(trace) - 1 : 
      a = net.g[i+1][0]
      b = net.g[i+1][1]
      relylist = trim(graphlist[i].segments, ylist[i], gamma[i+1] - b, gamma[i+1] -a)[0]
      relgraph = trim(graphlist[i].segments, ylist[i], gamma[i+1] -b, gamma[i+1] -a)[1]
      for j in range(len(relgraph)) : 
        if relgraph[j][1] < 0 : 
          nadir = j
    else : 
      relylist = ylist[i]
      relgraph = graphlist[i].segments
      nadir = graphlist[i].nadir
    ydeclist = relylist[:nadir]
    yinclist = relylist[nadir:]
    if binary(yrev(ydeclist), cost) != None : 
      k = len(ydeclist) -1 - binary(yrev(ydeclist), cost)
    elif binary(yinclist, cost) != None : 
      k = len(ydeclist) + binary(yinclist, cost)
    xsegment = relgraph[k]
    val = 0
    if xsegment[1] == 0 : 
      val = xsegment[0]
    else : 
      val = xsegment[0] + (cost-relylist[k][0])/(xsegment[1])
    gamma[i] = val
    
    cost = cost - abs(gamma[i] - trace[i])
    i = i-1
  return gamma
