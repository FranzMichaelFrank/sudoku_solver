from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
import random
from random import sample

def initialize_population(size, difficulty):
    """This function initializes a populattion of given size for randomly filled sudoku puzzles with given difficulty!"""
    
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