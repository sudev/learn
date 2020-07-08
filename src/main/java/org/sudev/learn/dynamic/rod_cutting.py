from typing import Mapping, List

## CLRS - 15.1 Rod Cutting
# length -> price
price_map = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}

# Own code
def rod_cutting(price_map: Mapping[int, int]) -> Mapping[int, int]:
    sub_problem_price_cache: Mapping[int, int] = {}
    for outer_pos in range(1, len(price_map) + 1):
        # Assign the max price as that of the rod without cutting
        max_price = price_map[outer_pos]
        # Iterate every cutting option till outer_pos
        for inner_pos in range(1, outer_pos):
            # Reuse the subproblem solutions calculated before
            price = sub_problem_price_cache[inner_pos] + sub_problem_price_cache[outer_pos - inner_pos]
            if (price > max_price):
                max_price = price
        sub_problem_price_cache[outer_pos] = max_price
    return sub_problem_price_cache
print(rod_cutting(price_map))

# Above using recursion 
def rod_cutting_recursion(price_map: Mapping[int, int], n: int, cache: List[int]) -> int:
    if n == 0:
        return 0
    if (cache[n-1] > 0):
        return cache[n-1]
    options = []
    for pos in range(1, n + 1):
        options.append(price_map[pos] + rod_cutting_recursion(price_map, n - pos, cache))
    cache[n-1] = max(options)
    return max(options)

print(rod_cutting_recursion(price_map, 5,[0]*5))


# Rod cutting recursive top-down 
# No optimisation, will be called 2*exp(N) times 
# Naive solution without DP
def rod_cut_recursive_top_down(price_map: Mapping[int, int], n: int) -> Mapping[int, int]:
    if n == 0:
        return 0
    q = -1000
    for pos in range(1, n):
         q = max(q, price_map[pos] + rod_cut_recursive_top_down(price_map, n - pos))
    return q
