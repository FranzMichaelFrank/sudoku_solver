import random
from random import sample

def create_sudoku(difficulty):
    """This function creates a sudoku puzzle for a given difficulty. The difficulty has to be expressed as a string and can either
    be "easy", "medium" or "hard"."""
    
    def maths(row,col):
        """This function returns a number between 0 and 8, depending on the numbers it is given"""
        return (3 * (row % 3) + row // 3 + col) % 9

    #create a list with the 3 sequences [0,1,2], [3,4,5], [6,7,8] shuffled but always staying together as shuffled sequences of 3
    rows = [n * 3 + row for n in sample(range(3), 3) for row in sample(range(3), 3)] 

    #create another list with the 3 sequences [0,1,2], [3,4,5], [6,7,8] shuffled but always staying together as shuffled sequences of 3
    columns = [n * 3 + col for n in sample(range(3), 3) for col in sample(range(3), 3)]

    #create a list with unique digits from 1 to 9 in a random order
    one_to_nine = sample(range(1,10), 9)

    #create a valid sudoku solution by using the two lists created above
    #the solve function in combination with the kept sequences of the three consecutive numbers make sure that the solution is valid
    #a sudoku solution is valid, if there are no duplicates within rows, columns and blocks
    sudoku_solved = [[one_to_nine[maths(row,col)] for col in columns] for row in rows]
    
    #define the number of fields to keep according to the given difficulty
    if difficulty == "easy":
        to_delete = random.randint(49,53)
    elif difficulty == "medium":
        to_delete = random.randint(54,58)
    elif difficulty == "hard":
        to_delete = random.randint(59,62)
    else:
        raise Exception("You must specify the difficulty as 'easy', 'medium' or 'hard'!")
    
    #deleting random fields of the valid solution, by setting them to 0
    for field in sample(range(81),to_delete):
        sudoku_solved[field // 9][field % 9] = 0
    
    #return the sudoku matrix with certain deleted field according to the wanted level of difficulty
    return [item for sublist in sudoku_solved for item in sublist] 


def display_sudoku(sudoku, initial_sudoku=None):
    """This function displays a sudoku puzzle in a pretty way!"""
    
    if initial_sudoku == None:
        sudoku_matrix = [sudoku[i:i+9] for i in range(0,len(sudoku),9)]
    else:
        sud_full = []
        count_sol = 0
        for element in initial_sudoku:      
            if element == 0:
                sud_full.append(sudoku[count_sol])
                count_sol += 1
            else:
                sud_full.append(element)
        sudoku_matrix = [sud_full[i:i+9] for i in range(0,len(sud_full),9)]
        
    
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(3-1)]*3)+line[9:13]

    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""]+[symbol[n] for n in row] for row in sudoku_matrix]
    
    print(line0)
    
    for r in range(1,10):
        print("".join(n+s for n,s in zip(nums[r-1],line1.split("."))))
        print([line2,line3,line4][(r%9==0)+(r%3==0)])