from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
from fitness_function import fitness_score
import random
from random import sample

def initialize_population(size, difficulty):
    """This function initializes a populattion of given size for randomly filled sudoku puzzles with given difficulty!"""
    
    #generate the puzzle which will be filled with random values "size" times
    sudoku = create_sudoku(difficulty)

    population = []

    #generate random solutions and store them in the population list
    for i in range(size):

        generated_solution = []

        for sublist in sudoku:
            generated_solution.append([i if i != 0 else random.randint(1,9) for i in sublist ])

        population.append(generated_solution)
        
    return population