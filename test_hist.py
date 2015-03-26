import Pmf
import matplotlib.pyplot as pyplot

vals, freqs = hist.Render()
rectangles = pyplot.bar(vals, freqs)
pyplot.show()
