from charles.charles import Population, Individual
from charles.selection import fps, tournament, rank
from charles.mutation import swap_mutation, binary_mutation, inversion_mutation, distinct_mutation
from charles.crossover import cycle_co, single_point_co, arithmetic_co, pmx_co
from sudoku_generator import create_sudoku
from sudoku_generator import display_sudoku
from initialize_population import initialize_population
import random
import time
from random import choices
from random import sample
from copy import deepcopy
import pandas as pd


def evaluate_270(sudoku, initial_sudoku):
    """This fitness function computes fitness scores for solved Sudokus. For each row, column and block the score is increased
        with the respective number of distinct digits within that particular row, column or block. Additionally, every fully distinct
        row, column or block gets one extra point. The maxmimum score that can be reached is 270.

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


def evaluate_243(sudoku, initial_sudoku):
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

#the following lines can be used for measuring the runtime
#start = time.time()
#print("START")

#Monkey patching
Individual.evaluate = evaluate_243
Individual.get_neighbours = get_neighbours

fitness_scores_easy = []
fitness_scores_medium = []
fitness_scores_hard = []

#repeat the following process 75 times (25 each per difficulty level)
for i in range(75):

    
    pop_size = 200000

    #initialize a sudoku and a population of random solutions for it for particular difficulty
    if i < 25:
        sudoku_and_population = initialize_population(pop_size,"easy")
    elif i < 50:
        sudoku_and_population = initialize_population(pop_size,"medium")
    else:
        sudoku_and_population = initialize_population(pop_size,"hard")


    pop = Population(
        size=pop_size,
        optim="max",
        individuals=sudoku_and_population["population"],
        initial_sudoku=sudoku_and_population["sudoku"]
    )

    #evolve the population
    pop.evolve(
        gens=75,
        select=tournament, #fps #tournament #rank
        crossover=pmx_co, #single_point_co #cycle_co #pmx_co 
        mutate=swap_mutation, #inversion_mutation #swap_mutation #distinct_mutation
        co_p=0.8,
        mu_p=0.7,
        elitism=True
    )

    #get the solution with the highest fitness score
    max_fitness = 0
    max_position = 0

    for j in range(50):
        if pop[j].fitness > max_fitness:
            max_position = j
            max_fitness = pop[j].fitness

    if i < 25:
        fitness_scores_easy.append(max_fitness)
    elif i < 50:
        fitness_scores_medium.append(max_fitness)
    else:
        fitness_scores_hard.append(max_fitness)

#the following lines can be used for measuring the runtime
#end = time.time()
#print("END")
#print(end - start)

#store the results of all 75 rounds within a dataframe
results = pd.DataFrame([fitness_scores_easy,fitness_scores_medium,fitness_scores_hard], index=["easy", "medium", "hard"], columns = ["R_" + str(i+1) for i in range(25)])
results["Average_Fitness"] = results.T.mean()

#export the dataframe as csv
results.to_csv("tournament__pmx_co__swap_mutation__243__200000__co_p__0_8__mu_p__0_7__gens_75.csv")





