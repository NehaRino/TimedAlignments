#mixed align
def mixalign(net, obs): 
  n = net.l
  proc = [0]
  obs.insert(0,0)
  for i in range(n) : 
    a = net.g[i][0]
    b = net.g[i][1]
    flow = obs[i+1] - obs[i]
    if flow < a : 
      proc.append(proc[i] + a)
    elif flow <= b : 
      proc.append(proc[i] + flow)
    else : 
      proc.append(proc[i] + b)
    
  proc = proc[1:]
  obs = obs[1:]
  cost = mixbackward(obs, proc)
  return cost, proc
