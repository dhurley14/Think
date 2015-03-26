import math
from libs import survey
from libs.thinkstats import MeanVar
from libs.first_answer import PartitionRecords
from libs import myplot
from libs import Pmf

table = survey.Pregnancies()
table.ReadRecords()

first_recs, other_recs = PartitionRecords(table)  # returns two tables.

# Compute s.d. of first recs and sec_recs

weeks1 = [record.prglength for record in first_recs.records]
weeks_others = [record.prglength for record in other_recs.records]

mu1, var1 = MeanVar(weeks1)
mu2, var2 = MeanVar(weeks_others)

hist1 = Pmf.MakeHistFromList(weeks1)
hist_others = Pmf.MakeHistFromList(weeks_others)

axis = [23, 46, 0, 2700]
myplot.Hists([hist1, hist_others])
#myplot.Save(root='nsfg_hist', 
#                title='Histogram',
#                xlabel='weeks',
#                ylabel='frequency',
#                axis=axis)

#hists = [hist1, hist_others]
#myplot.Hist(hist1)
