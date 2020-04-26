#!/usr/bin/python3
""" Tests for Tower of Hanoi """
import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tower_of_hanoi import Hanoi

def test_hanoi(disks=10):
    """ Test state of towers before and after solving """
    t = Hanoi(disks, verbose=False)
    assert t.tower == {'a': list(range(disks, 0, -1)), 'b': [], 'c': []}
    t.solve_hanoi()
    assert t.tower == {'a': [], 'b': [], 'c': list(range(disks, 0, -1))}

if __name__ == '__main__':
    t0 = datetime.now()
    for n in range(1, 20):
        test_hanoi(n)
    t1 = datetime.now()
    print(f"Finished tests in {t1 - t0}")
