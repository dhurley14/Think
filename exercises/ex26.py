import math
from libs import Pmf
from libs import descriptive
""" calculate the probability of a baby being born on time
(Weeks 38, 39, 40), early (t <= 37) or late (t >= 41)

Make Three PMF's, one for the first baby's and one for the others,
then one for all live births.

"""


def ProbEarly(Pmf):
    # calc prob child from before week 37
    return CalcProb(Pmf, 0, 37)


def ProbOnTime(Pmf):
    return CalcProb(Pmf, 38, 40)


def ProbLate(Pmf):
    return CalcProb(Pmf, 41, 50)


def CalcProb(Pmf, start_week, end_week):
    # Calculate probability of a birth
    # occurring between the start
    # and end weeks.
    prob = 0.0
    for item in Pmf.Items():
        if item[0] >= start_week and item[0] <= end_week:
            prob += Pmf.Prob(item[0])

    return prob


if __name__ == '__main__':
    pool, first_babies, other_babies = descriptive.MakeTables()

    prob_e_first = ProbEarly(first_babies.pmf)
    prob_ot_first = ProbOnTime(first_babies.pmf)
    prob_late_first = ProbLate(first_babies.pmf)

    prob_e_others = ProbEarly(other_babies.pmf)
    prob_ot_others = ProbOnTime(other_babies.pmf)
    prob_late_others = ProbLate(other_babies.pmf)

    print("first early: " + str(prob_e_first) + " on time: " +
          str(prob_ot_first) + " late: " + str(prob_late_first))
    print("others early: " + str(prob_e_others) + " on time: " +
          str(prob_ot_others) + " late: " + str(prob_late_others))

    # calculate the relative risks.
    print("relative risk of first baby being born early: " +
          str(prob_e_first/prob_e_others))
    print("relative risk of first baby being born late: " +
          str(prob_late_first/prob_late_others))
