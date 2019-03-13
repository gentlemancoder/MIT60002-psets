###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import time
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
#   Quick and dirty greedy algorithm
    target_copy = target_weight
    start = time.time()
    eggs = sorted(egg_weights, reverse=True)
    for egg in eggs:
        num_eggs = target_copy // egg
        memo[egg] = num_eggs
        target_copy = target_copy - num_eggs * egg
    print(sum(memo.values()))
    end = time.time()
    print(end-start)
#   Dynamic solution, bottom up:
#   
#   Set up dict so that with values larger than the target for comparision
#   purposes
#    start = time.time()
#    for weight in range(target_weight +1):
#        memo[weight] = target_weight + 1
#    memo[0] = 0    # 0 is always 0 no matter which coin is used
#
#    for weight in range(target_weight+1):       
#
#        for egg in egg_weights:
##        
#            if egg <= weight:          
#                memo[weight] = min(memo[weight], memo[weight-egg] + 1)
##  
#    print(memo[target_weight])
#    end = time.time()
#    print(end-start)
#    

def td_make_weight(egg_weights, target_weight, memo = {}):
    #    Top down implementation:
    memo[0] = 0
    
    if target_weight == 0:
        return 0
    elif target_weight < 1:
        return -1
    elif target_weight == 1:
        return 1
    
    if target_weight - 1 in memo:
        return memo[target_weight - 1]
    
    minimum = target_weight + 1
    for egg in egg_weights:
        result = td_make_weight(egg_weights, target_weight - egg, memo)
        if result >= 0 and result < minimum:
            minimum = result +1
        
    if minimum < target_weight + 1:
        memo[target_weight - 1] = minimum

    
    return memo[target_weight-1]


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    start = time.time()
    print(td_make_weight([1,5,10,25],99))
    end = time.time()
    print(end-start)