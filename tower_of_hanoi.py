#!/usr/bin/python3
''' Tower of Hanoi '''
import cProfile

class Hanoi():
    """ Tower of Hanoi Class """
    def __init__(self, disks=None, verbose=True):
        if disks:
            self.__disks = disks
            self.__verbose = verbose
            self.generate_tower(disks)

    def __move(self, tower, start, end):
        """ Move disks in tower from {start} to {end} """
        if self.__verbose:
            print(f"Move {tower[start][-1]} disks, from {start} --> {end}.")
        tower[end].append(tower[start].pop())
        if self.__verbose:
            print(tower, '\n')

    def __solve(self, tower, start, via, end, disks):
        """ Actual algorithm for solving """
        if disks > 0:
            self.__solve(tower, start, end, via, disks - 1)
            self.__move(tower, start, end)
            self.__solve(tower, via, start, end, disks - 1)


    def solve_hanoi(self):
        """ Wrapper to input arguments """
        self.__solve(tower=self.__tower, start='a', via='b', end='c', disks=self.__disks)

    def generate_tower(self, disks=0):
        """ Generates new Tower of Hanoi given {disks:int} """
        tower = {
            'a': list(range(disks, 0, -1)),
            'b': [],
            'c': [],
        }
        self.__tower = tower

    @property
    def tower(self):
        """ Returns the current state of the Hanoi Tower """
        return self.__tower


if __name__ == '__main__':
    N = 5
    T = Hanoi(N)
    print(f"Start:\n{T.tower}\n")
    T.solve_hanoi()
    print(f"End:\n{T.tower}\n")

    T.generate_tower(N)

    cProfile.run("""T.solve_hanoi()""")
