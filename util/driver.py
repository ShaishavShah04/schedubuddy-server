from permutation import permute_classes
from draw_sched import draw_schedule

schedules = permute_classes(["CMPUT 355"])

first_sched = schedules[0]
print(first_sched)

draw_schedule(first_sched)