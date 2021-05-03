from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from charles.selection import fps, tournament
from charles.mutation import swap_mutation, binary_mutation, inversion_mutation
from charles.crossover import cycle_co, single_point_co, arithmetic_co
from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
from initialize_population import initialize_population
import random
from random import choices
from random import sample
from copy import deepcopy


def evaluate(sudoku, initial_sudoku):
    """Describe function

    Returns:
        
    """
    
    sud_full = []
    count_sol = 0
    for element in initial_sudoku:      
        if element == 0:
            sud_full.append(sudoku[count_sol])
            count_sol += 1
        else:
            sud_full.append(element)
    sudoku_matrix = [sud_full[i:i+9] for i in range(0,len(sud_full),9)]
    
    fitness_score = 0

    #get fitness of rows
    for row in range(9):
        if len(set(sudoku_matrix[row])) == 9:
            fitness_score += len(set(sudoku_matrix[row])) + 1
        else:
            fitness_score += len(set(sudoku_matrix[row]))

    #get fitness of columns
    for col in range(9):
        column = []
        for row in range(9):
            column.append(sudoku_matrix[row][col])

        if len(set(column)) == 9:
            fitness_score += len(set(column)) + 1
        else:
            fitness_score += len(set(column))

    #get fitness of blocks
    for element in [[sudoku_matrix[i][j] for i in range(0,3) for j in range(0,3)], [sudoku_matrix[i][j] for i in range(3,6) for j in range(0,3)],
                    [sudoku_matrix[i][j] for i in range(6,9) for j in range(0,3)], [sudoku_matrix[i][j] for i in range(0,3) for j in range(3,6)],
                    [sudoku_matrix[i][j] for i in range(3,6) for j in range(3,6)], [sudoku_matrix[i][j] for i in range(6,9) for j in range(3,6)],
                    [sudoku_matrix[i][j] for i in range(0,3) for j in range(6,9)], [sudoku_matrix[i][j] for i in range(3,6) for j in range(6,9)],
                    [sudoku_matrix[i][j] for i in range(6,9) for j in range(6,9)]]:
        if len(set(element)) == 9:
            fitness_score += len(set(element)) + 1
        else:
            fitness_score += len(set(element))
    
    return fitness_score


def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    pass

# Monkey patching
Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours

# Initialize a sudoku and a population of random solutions for it
pop_size = 10000
sudoku_and_population = initialize_population(pop_size,"easy")

pop = Population(
    size=pop_size,
    optim="max",
    individuals=sudoku_and_population["population"],
    initial_sudoku=sudoku_and_population["sudoku"]
    #**kwargs
    #valid_set=[i for i in range(1,10)]
    #replacement=True
    #dynamic length of solution
)

pop.evolve(
    gens=100,
    select=tournament,
    crossover=single_point_co,
    mutate=swap_mutation,
    co_p=0.7,
    mu_p=0.2,
    elitism=True
)


#display_sudoku(pop[0], sudoku_and_population["sudoku"])
