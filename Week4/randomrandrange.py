import random
from datetime import datetime, timedelta

random_int_0_to_5 = random.randrange(0, 6)
print("Random Integer between 0 and 5 (excluding 6):", random_int_0_to_5)

random_int_5_to_9 = random.randrange(5, 10)
print("Random Integer between 5 and 9 (excluding 10):", random_int_5_to_9)

random_int_0_to_10_step_3 = random.randrange(0, 11, 3)
print("Random Integer between 0 and 10 with a step of 3:", random_int_0_to_10_step_3)

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 10)
random_date = start_date + timedelta(days=random.randrange((end_date - start_date).days))
print("Random Date between {} and {}: {}".format(start_date.date(), end_date.date(), random_date.date()))
