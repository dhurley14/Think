import math
import survey
from thinkstats import MeanVar
from first_answer import PartitionRecords

table = survey.Pregnancies()
table.ReadRecords()

first_recs, other_recs = PartitionRecords(table)  # returns two tables.

# Compute s.d. of first recs and sec_recs

weeks1 = [record.prglength for record in first_recs.records]
weeks_others = [record.prglength for record in other_recs.records]

mu1, var1 = MeanVar(weeks1)
mu2, var2 = MeanVar(weeks_others)

sd1 = math.sqrt(var1)
sd2 = math.sqrt(var2)

print("standard deviation of first births.. ", sd1)
print("standard deviation of post-initial births.. ", sd2)
