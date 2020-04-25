#!/usr/bin/python3
''' factorial methods with bench marks '''

import cProfile
from memory_profiler import memory_usage
import sys
sys.setrecursionlimit(3000)

def factorial_recursion(n): # slowest
    if n <= 1:
        return 1    
    return n * factorial_recursion(n-1)

def factorial_recursion_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = factorial_recursion_memo(n-1, memo) * n
        memo[n] = x
        return x
               
def factorial_iter(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

if __name__ == '__main__':
    n = 2000
    assert factorial_recursion(n) == factorial_recursion_memo(n) == factorial_iter(n)
    # runtimes
    cProfile.run('factorial_recursion(n)')
    cProfile.run('factorial_recursion_memo(n)')
    cProfile.run('factorial_iter(n)')
    
    # memory usage
    results1 = memory_usage((factorial_recursion, (n,)))
    results2 = memory_usage((factorial_recursion_memo, (n,)))
    results3 = memory_usage((factorial_iter, (n,)))
    print(f"max: {max(results1):0.2f},\tmin: {min(results1):0.2f},\tsum: {sum(results1):0.2f},\tcount: {len(results1)}")
    print(f"max: {max(results2):0.2f},\tmin: {min(results2):0.2f},\tsum: {sum(results2):0.2f},\tcount: {len(results2)}")
    print(f"max: {max(results3):0.2f},\tmin: {min(results3):0.2f},\tsum: {sum(results3):0.2f},\tcount: {len(results3)}")