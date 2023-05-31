import math

def chocolateFeast(money, cost, wrappers):
    bars = math.floor(money/cost)
    remaining_wrappers = bars
    
    while remaining_wrappers >= wrappers:
        extra_bars = math.floor(remaining_wrappers/wrappers)
        remaining_wrappers = extra_bars + remaining_wrappers%wrappers
        bars += extra_bars
        
    return bars
    
print(chocolateFeast(15, 3, 2))