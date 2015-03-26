from libs import Pmf


data = [1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6, 8]
pmf = Pmf.MakePmfFromList(data)

mu = 0.0
s2 = 0.0

for item in pmf.Items():
    mu += pmf.Prob(item[0])*item[0]

print("mu: ", mu)

for item in pmf.Items():
    s2 += pmf.Prob(item[0])*((item[0] - mu)**2)

print("sigma^2: ", s2)
