from libs import Pmf
import sys


def ConditionalProb(Pmf, x):
    # computes probability of an event occurring after some period x
    new_pmf = get_new_pmf(Pmf, x)
    asum = sum([new_pmf.Prob(item[0]) for item in new_pmf.Items()])
    return asum


def get_new_pmf(Pmf, x):
    # Create a new PMF
    # Where only considers values
    # after week x.

    [Pmf.Remove(item[0]) for item in Pmf.Items() if item[0] <= x]
    # Pmf.Normalize()
    return Pmf


if __name__ == '__main__':
    data = [0.1, 0.1, 0.1, 0.2, 1, 2, 2, 2, 3, 3, 3, 3, 4]
    pmf = Pmf.MakePmfFromList(data)
    print(ConditionalProb(pmf, float(sys.argv[1])))
