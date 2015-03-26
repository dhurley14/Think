import math
from thinkstats import Var, Mean

DATA = [1,2,3,3,4]
sigma_2 = Var(DATA)
mu = Mean(DATA)
sigma = math.sqrt(sigma_2)

print("variance: ", sigma_2)
print("mean: ", mu)
print("s.d.: ", sigma)
