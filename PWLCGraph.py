import copy 
#an object to handle piecewise-linear convex graphs 
class PWLCGraph : 
  #start with the zero function on the appropriate domain 
  def __init__(self, domain): 
    self.left = domain[0]
    self.right = domain[1]
    self.segments = [[self.left, 0, self.right]]
    #nadir is the rightmost endpoint of a negative slope segment, where the next flat segment should start
    self.nadir = 0 
    #begin stores the height of the leftmost point of the curve
    self.begin = 0 

  def __repr__(self) : 
    return repr(self.segments)

  def insertflatseg(self, length): 
    i = self.nadir  
    flag = 0
    if i == len(self.segments) : 
      low = self.right 
      self.segments.append([low, 0, low + length])
    else : 
      while i < len(self.segments): 
        if self.segments[i][1] == 0: 
          self.segments[i][2] = self.segments[i][2] + length 
          flag = 1 
        elif flag == 0 and self.segments[i][1] > 0 : 
          low = self.segments[i][0]
          slope = 0 
          high = low + length 
          self.segments.insert(i, [low, slope, high])
          flag = 1
        else : 
          self.segments[i][0] = self.segments[i][0] + length 
          self.segments[i][2] = self.segments[i][2] + length
        i = i+1
    self.right = self.right + length

  def min(self, interval) : 
    a = interval[0]
    b = interval[1]
    i = 0 
    for i in range(len(self.segments)): 
      self.segments[i][0] = self.segments[i][0] + a
      self.segments[i][2] = self.segments[i][2] + a
    self.left = self.left + a
    self.right = self.right + a
    if b != a : 
      self.insertflatseg(b-a)

  def addmod(self, pivot) : 
    a = self.left 
    b = self.right 
    i = 0 
    self.begin = self.begin + abs(a - pivot)
    while i < len(self.segments): 
      if self.segments[i][2] <= pivot : 
        self.segments[i][1] = self.segments[i][1] - 1
      elif self.segments[i][0] < pivot and self.segments[i][2] > pivot : 
        slope = self.segments[i][1]
        low = self.segments[i][0]
        high = self.segments[i][2]
        self.segments.insert(i+1, [pivot, slope, high])
        self.segments[i][2] = pivot
        self.segments[i][1] = slope - 1
      else : 
        self.segments[i][1] = self.segments[i][1] + 1
      i = i+1
    i = 0 
    while i < len(self.segments) and self.segments[i][1] < 0 : 
      i = i + 1
    self.nadir = i
