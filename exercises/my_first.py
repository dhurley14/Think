from libs import survey

table = survey.Pregnancies()
table.ReadRecords()

print(table.GetFields())

NUM_PREGNANCIES = 13593.0
live_birth_count_first_child = 0
live_birth_count_second_child = 0

first_avg_preg = []
second_avg_preg = []  # avg preg length for second, third, fourth child born

for record in table.records:
    if record.outcome == 1 and record.birthord == 1:

        live_birth_count_first_child += 1
        first_avg_preg.append(record.prglength)

    elif record.outcome == 1 and record.birthord > 1:

        live_birth_count_second_child += 1
        second_avg_preg.append(record.prglength)

print("first birth count..", live_birth_count_first_child)
print("first birth avg length: ",
      (sum(first_avg_preg))/float(len(first_avg_preg)))

print "second birth count..", live_birth_count_second_child
print("second birth avg length: ",
      (sum(second_avg_preg))/float(len(second_avg_preg)))
