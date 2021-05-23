from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
import random
from random import sample

def initialize_population(size, difficulty):
    """This function initializes a populattion of given size for randomly filled sudoku puzzles with given difficulty!

    Args:
        size (int): size of the population (=number of created solutions for one single Sudoku puzzle)
        difficulty (["easy", "medium", "hard"]): level of difficulty of the Sudoku puzzle

    Returns:
        {"population":population, "sudoku":sudoku}: a dictionary: the first key "population" corresponds to a value of a list
        containing the population instances as lists; the second key "sudoku" corresponds to a value of a single list containing
        the unsolved Sudoku puzzle
    """
    
    #generate the puzzle which will be filled with random values "size" times
    sudoku = create_sudoku(difficulty)
    sudoku_matrix = [sudoku[i:i+9] for i in range(0,len(sudoku),9)]

    population = []

    #generate random solutions and store them in the population list
    for i in range(size):

        generated_solution = []

        for sublist in sudoku_matrix:
            for i in sublist:
                if i==0:
                    generated_solution.append(random.randint(1,9))

        population.append(generated_solution)
        
    return {"population":population, "sudoku":sudoku}