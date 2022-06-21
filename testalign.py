import timeit 
import numpy as np
def randmodel(netsize, bound): 
  model = Linemodel(netsize)
  for i in range(model.l): 
    a = np.random.randint(bound)
    b = a + np.random.randint(bound)
    model.guard(i, a, b)
  return model

def teststamp(x, bound): 
  smodel = Linemodel(x)
  smodel = randmodel(x, bound)
  ss = list(np.random.randint(bound, size=x))
  ss.sort()
  rtime = timeit.timeit(lambda : stampcost(ss, smodel), number=10)
  result = (x, rtime/10)
  return result

def testmix(x, bound): 
  mmodel = randmodel(x, bound)
  ms = list(np.random.randint(bound, size=x))
  ms.sort()
  rtime = timeit.timeit(lambda : mixalign(ms, mmodel), number=100)
  result = (x, rtime/100)
  return result

bound = 1000000
testnum = [10, 100, 1000, 10000, 100000, 1000000]
print("Mixed Alignment Results : ")
for x in testnum:
  print(testmix(x, bound))
print("    ")
print("Stamp Alignment Results : ")
for x in testnum:
  print(teststamp(x, bound))
