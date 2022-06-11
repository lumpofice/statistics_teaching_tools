import getpass
import numpy as np
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s -'\
    ' %(message)s')


logging.debug('Start of Program')


def greedy_pig():
    """This function rolls a 6-sided die, according to user input, storing
each resulting face value that is not equal to 1. Users continue to play until
they either choose to quit or they roll a face value equal to 1. Users begin
each 'game' with a sum of 0. Each face value greater than 1 that is rolled
is stored into a list, and the current sum of the face values within that
list is computed. If users choose to quit before a face value of 1 is rolled,
the sum of all the face values from previous rolls will be computed and
return under the printed set of face values observed for those rolls. If users
roll a face value of 1, then whatever sum may have resulted from the user
choosing to forego a subsequent roll reverts back to zero."""
    
    
    # Face values different from 1 will be stored in here.
    faces = []
    
    
    # We define the array of choices from rolling this 6-sided die
    possible_outcomes = np.arange(1, 7)
    
    
    # We get the game started with a prompt to the user
    initial_query = getpass.getpass('Greedy Pig?'\
        ' Press return if you wish to exit.\nPress any other key,'\
        ' followed by the return key, if you wish to play.\n')
    
    
    # If user does not wish to play
    if not initial_query:
        return 'Goodbye'
    
    
    # If user does wish to play
    flag = True
    while flag:
        
        
        # Below, face will be the face value observed in the roll of the die
        face = np.random.choice(possible_outcomes, 1)
        
        
        # If the face value is 1, we must end the game and let the user know
        # how much they could have won had they not been so greedy
        if face == 1:
            return f'Just lost all of our points! '\
                f'Went from {sum(np.concatenate(faces))} to 0.'
        
        
        # If the face value is different from 1
        faces.append(face) 
        print(f'We rolled a {face.item()}.'\
            f'\nBrings us to a sum of {sum(np.concatenate(faces))}.\n')
        
        
        # We prompt the user to choose whether or not to play again
        subsequent_query = getpass.getpass('Roll again?'\
        ' Press return if you wish to exit.\nPress any other key,'\
        ' followed by the return key, if you wish to roll again.\n')
        
        
        # If the user wishes to walk away with winnings
        if not subsequent_query:
            flag = False
            continue
    
    
    # We consolidate all face values in a single list and print that list
    faces = np.concatenate(faces)
    print(f'We rolled the following set: {faces},')
    
    
    # Then we return the sum of that list
    return f'Giving us a total of {sum(faces)}'


greedy_pig()