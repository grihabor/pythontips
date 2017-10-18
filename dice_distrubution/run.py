from itertools import product
from pprint import pprint
from decimal import Decimal
from collections import Counter


options = range(1, 7)
outcomes = product(options,  repeat=3)
sum_outcomes = (sum(outcome) for outcome in outcomes)
c = Counter(sum_outcomes)
outcome_count = sum(c.values())
distribution = {
    key: value / outcome_count 
    for key, value in c.items()
}
pprint(distribution)

