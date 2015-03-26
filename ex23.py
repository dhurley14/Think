import math
import Pmf
import operator
from collections import OrderedDict


def mode(Hist):
    return Hist.MaxLike()


def AllModes(Hist):
    return OrderedDict(sorted(Hist.Items(), reverse=True,
                              key=operator.itemgetter(1)))

if __name__ == '__main__':
    hist = Pmf.MakeHistFromList(['a', 'b', 'b', 'c', 'd'])
    print AllModes(hist)
