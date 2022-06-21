#stamp only alignment algorithm, calculates minimum cost and aligning word
def stampcost(net, trace) : 
  graphlist = []
  a = net.g[0][0] 
  b = net.g[0][1]
  graph = PWLCGraph([a, b])
  graph.addmod(trace[0])
  g = copy.deepcopy(graph)
  graphlist.append(g)
  for i in range(1, net.l) : 
    a = net.g[i][0]
    b = net.g[i][1]
    graph.min([a,b])
    graph.addmod(trace[i])
    g = copy.deepcopy(graph)
    graphlist.append(g)
  s = graph.segments[0][1]
  k = 0 
  cost = graph.begin
  
  while k < graph.nadir: 
    s = graph.segments[k][1]
    cost = cost + (s*(graph.segments[k][2] - graph.segments[k][0]))
    k = k + 1
  gamma = backtrack(trace, graphlist, cost, net)
  return cost, gamma
