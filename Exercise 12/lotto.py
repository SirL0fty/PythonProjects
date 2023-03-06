#!/usr/bin/env python3

#* imports the random standard
import random

#*set's the variable and using random.sample I can set the range between any number and choose 6 in this case
lotto_numbers = random.sample(range(1, 51), 6)
print(lotto_numbers)