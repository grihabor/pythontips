from itertools import product
from pprint import pprint
from collections import Counter


distribution = (lambda c: {
    key: value / sum(c.values()) 
    for key, value in c.items()
})(Counter(
    sum(outcome) for outcome 
    in product(range(1, 7),  repeat=3)
))

pprint(distribution)
#>{3: 0.004629629629629629,
#> 4: 0.013888888888888888,
#> 5: 0.027777777777777776,
#> 6: 0.046296296296296294,
#> 7: 0.06944444444444445,
#> 8: 0.09722222222222222,
#> 9: 0.11574074074074074,
#> 10: 0.125,
#> 11: 0.125,
#> 12: 0.11574074074074074,
#> 13: 0.09722222222222222,
#> 14: 0.06944444444444445,
#> 15: 0.046296296296296294,
#> 16: 0.027777777777777776,
#> 17: 0.013888888888888888,
#> 18: 0.004629629629629629}
