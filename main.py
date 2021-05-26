from charles.charles import Population, Individual
from charles.selection import fps, tournament, rank
from charles.mutation import swap_mutation, binary_mutation, inversion_mutation, distinct_mutation
from charles.crossover import cycle_co, single_point_co, arithmetic_co, pmx_co
from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
from initialize_population import initialize_population
import random
from random import choices
from random import sample
from copy import deepcopy


def evaluate(sudoku, initial_sudoku):
    """This fitness function computes fitness scores for solved Sudokus. For each row, column and block the score is increased
        with the respective number of distinct digits within that particular row, column or block. The maxmimum score that can be 
        reached is 243.

    Args:
        sudoku: a list that corresponds to a solution for a Sudoku puzzle
        initial_sudoku: a list that corresponds to an unsolved Sudoku puzzle for which "sudoku" is the solution


    Returns:
        fitness_score (int): a fitness score for a Sudoku solution
        
    """
    
    #build the full Sudoku matrix from the given puzzle and solution
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
        
        fitness_score += len(set(sudoku_matrix[row]))

    #get fitness of columns
    for col in range(9):
        column = []
        for row in range(9):
            column.append(sudoku_matrix[row][col])
        
        fitness_score += len(set(column))

    #get fitness of blocks
    for element in [[sudoku_matrix[i][j] for i in range(0,3) for j in range(0,3)], [sudoku_matrix[i][j] for i in range(3,6) for j in range(0,3)],
                    [sudoku_matrix[i][j] for i in range(6,9) for j in range(0,3)], [sudoku_matrix[i][j] for i in range(0,3) for j in range(3,6)],
                    [sudoku_matrix[i][j] for i in range(3,6) for j in range(3,6)], [sudoku_matrix[i][j] for i in range(6,9) for j in range(3,6)],
                    [sudoku_matrix[i][j] for i in range(0,3) for j in range(6,9)], [sudoku_matrix[i][j] for i in range(3,6) for j in range(6,9)],
                    [sudoku_matrix[i][j] for i in range(6,9) for j in range(6,9)]]:
        
        fitness_score += len(set(element))
    
    return fitness_score

#there is no need for a neighbourhood function for the underlying problem
def get_neighbours(self):
    pass

#monkey patching
Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours

#initialize a Sudoku and a population of random solutions for it

pop_size = 200000
#the difficulty can be set in the following line
sudoku_and_population = initialize_population(pop_size,"easy")

pop = Population(
    size=pop_size,
    optim="max",
    individuals=sudoku_and_population["population"],
    initial_sudoku=sudoku_and_population["sudoku"],
)

#evolve the population
pop.evolve(
    gens=75,
    select=tournament,
    crossover=pmx_co,
    mutate=swap_mutation,
    co_p=0.8,
    mu_p=0.7,
    elitism=True
)

#display the empty Sudoku puzzle
display_sudoku(sudoku_and_population["sudoku"])

#get the solution with the highest fitness score
max_position = 0
max_fitness = 0

for j in range(pop_size):
    if pop[j].fitness > max_fitness:
        max_position = j
        max_fitness = pop[j].fitness

#display the solved Sudoku puzzle
display_sudoku(pop[max_position], sudoku_and_population["sudoku"])
