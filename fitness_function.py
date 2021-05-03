def fitness_score(population):
    """This function returns the fitness score as a dictionary!"""
    
    fitness_scores = {}
    
    for number in range(len(population)):
        
        sudoku = population[number]
        fitness_score = 0

        #get fitness of rows
        for row in range(9):
            if len(set(sudoku[row])) == 9:
                fitness_score += len(set(sudoku[row])) + 1
            else:
                fitness_score += len(set(sudoku[row]))

        #get fitness of columns
        for col in range(9):
            column = []
            for row in range(9):
                column.append(sudoku[row][col])
            
            if len(set(column)) == 9:
                fitness_score += len(set(column)) + 1
            else:
                fitness_score += len(set(column))
                
        #get fitness of blocks
        for element in [[sudoku[i][j] for i in range(0,3) for j in range(0,3)], [sudoku[i][j] for i in range(3,6) for j in range(0,3)],
                        [sudoku[i][j] for i in range(6,9) for j in range(0,3)], [sudoku[i][j] for i in range(0,3) for j in range(3,6)],
                        [sudoku[i][j] for i in range(3,6) for j in range(3,6)], [sudoku[i][j] for i in range(6,9) for j in range(3,6)],
                        [sudoku[i][j] for i in range(0,3) for j in range(6,9)], [sudoku[i][j] for i in range(3,6) for j in range(6,9)],
                        [sudoku[i][j] for i in range(6,9) for j in range(6,9)]]:
            if len(set(element)) == 9:
                fitness_score += len(set(element)) + 1
            else:
                fitness_score += len(set(element))
            
        fitness_scores[number] = fitness_score
    
    return fitness_scores
    