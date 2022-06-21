#this is the linear causal process of a tpn without and branches or synchrony
#essentially an unrolled automaton run, remembering the guards checked along the way 

class Linemodel : 
  def __init__(self, length):
    self.l = length
    self.g = [None]*self.l

  def guard(self, pos, eft, lft):
    self.g[pos] = (eft, lft)

  def run(self, word): 
    i = 0
    prev = 0
    for x in word : 
      if (x - prev) > self.g[i][1] or (x - prev) < self.g[i][0] :  
        return "reject"
        break 
      prev = x
      i = i+1
    return "accept"
