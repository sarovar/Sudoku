import sys 	
import time 
from Constraint_satisfaction import csp
from Backtrack_Algorithm import *

if __name__ == "__main__":

    if len(sys.argv)==2:
        grid = sys.argv[1]
        assert len(grid) == 81
        start = time.time()
        sudoku = csp(grid=grid)
        solved = Backtracking_Search(sudoku)


        if solved != "FAILURE":
            display(solved) 	
            print("Perfectly solved")
        else:
            print("Not solved")
    else:
        print("INVALID NUMBER OF INPUTS") 