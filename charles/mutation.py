from random import randint, sample
import random

def template_mutation(individual):
    """[summary]

    Args:
        individual ([type]): [description]

    Returns:
        [type]: [description]
    """
    return individual


def binary_mutation(individual):
    """Binary muation for a GA individual

    Args:
        individual (Individual): A GA individual from charles libray.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary."
        )

    return individual

def distinct_mutation(individual):
    """This function mutates an individual by randomly choosing a mutation point and subsequently exchanging its value 
        with that of another random point. This happens under the condition that the new value with which the initially 
        selected value is exchanged is neither the same as the initial one nor as the four nearest neighbors, which are the 2 
        values before and after, of the initial one.

    Args:
        individual (Individual): A GA individual from charles libray.py

    Returns:
        Individual: Mutated Individual
    """
        
    mut_point = randint(0, len(individual) - 1)

    close_points_and_self = []

    try:
        for i in [mut_point-2, mut_point-1, mut_point, mut_point+1, mut_point+2]:
            close_points_and_self.append(individual[i])
    except:
        pass
    
    change_partner = randint(0, len(individual) - 1)
    new_value = individual[change_partner]

    if new_value not in close_points_and_self:
        individual[change_partner] = individual[mut_point]
    else:
        while new_value in close_points_and_self:
            change_partner = randint(0, len(individual) - 1)
            new_value = individual[change_partner]
        individual[change_partner] = individual[mut_point]

    individual[mut_point] = new_value

    return individual

def swap_mutation(individual):
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Rename to shorten variable name
    i = individual

    i[mut_points[0]], i[mut_points[1]] = i[mut_points[1]], i[mut_points[0]]

    return i

def inversion_mutation(individual):
    i = individual
    # Position of the start and end of substring
    mut_points = sample(range(len(i)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    i[mut_points[0]:mut_points[1]] = i[mut_points[0]:mut_points[1]][::-1]

    return i
    
if __name__ == '__main__':
    i1 = [1,2,3,4,5,6]

    print(inversion_mutation(i1))