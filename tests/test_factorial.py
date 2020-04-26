#!/usr/bin/python3
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import factorial

def test_factorial_of_zero():
    n = 0
    assert factorial.factorial_recursion(n) == 1
    assert factorial.factorial_recursion_memo(n) == 1
    assert factorial.factorial_iter(n) == 1

def test_factorial_of_one():
    n = 1
    assert factorial.factorial_recursion(n) == 1
    assert factorial.factorial_recursion_memo(n) == 1
    assert factorial.factorial_iter(n) == 1
    
def test_factorial_of_10():
    n = 10
    ans = 3628800
    assert factorial.factorial_recursion(n) == ans
    assert factorial.factorial_recursion_memo(n) == ans
    assert factorial.factorial_iter(n) == ans
    
def test_factorial_of_neg():
    n = -1
    ans = None
    assert factorial.factorial_recursion(n) == ans
    assert factorial.factorial_recursion_memo(n) == ans
    assert factorial.factorial_iter(n) == ans
    
    
    
if __name__ == '__main__':
    test_factorial_of_zero()
    test_factorial_of_one()
    test_factorial_of_10()
    test_factorial_of_neg()
    