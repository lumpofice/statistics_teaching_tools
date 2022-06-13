import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True

logging.debug('Start of Program')


def dice_rolled(dice=1, rolls=1):
    """This function rolls for us a die, storing 100000 rolls 
    of that die into an array. Determined by 
    user input, this process happens a number of times 
    (the number of times representing the number of dice), wherein each
    array created is added to the array preceding it. Each 'time'
    throughout this process represents a single die, which is 
    rolled 100000 times, face values of which are stored in an array.
    The program begins with a row of zeros with 100000 columns."""
    
    
    # We start our program with a row of 100000 zeros
    X = np.zeros(rolls)
    
    
    # We run a for loop, with each run generating a row of 100000
    # face values
    for die in range(dice):
        faces = np.arange(1, 7)
        observations = np.random.choice(faces, rolls, replace=True)
        X += observations
        
        
    return X


def dice_distribution():
    """This function will determine the number of dice the user
    wishes to roll, and it will construct for us the distribution
    followed by the random variable that is the sum of all of those
    die. We preset the number of rolls for those user-determined
    number of die because we wish to simulate the theoretical 
    distribution."""
    
    
    # The process of gathering acceptable user input runs on a 
    # while loop
    flag = True
    while flag:
        
        
        # Here we gather user input
        dice_input = input('How many dice?'\
            ' Or press return to ext: ')
        
        
        # In case the user wishes to exit
        if not dice_input:
            return 'Goodbye'
        
        
        # If the user wishes not to exit, we check that their
        # input is acceptable
        try:
            dice = int(dice_input)
            if dice < 1:
                logging.debug('We need a positive integer.')
                continue
            
            
            # Once user input is determined acceptable, we
            # construct our distribution
            X = dice_rolled(dice, 100000)
            
            
            # Here, we plot the distribution we've constructed
            y = list(range(dice, 6*dice+2))
            fig, ax = plt.subplots(figsize=(15, 10))
            ax.hist(X, y, ec='k')
            plt.xlabel('Sum of Face Vaues', fontsize=20)
            plt.ylabel('Number of Times Sum Observed', fontsize=20)
            plt.xticks(fontsize=20)
            plt.yticks(fontsize=20)
            fig.suptitle(f'Distribution of Rolling {dice} Dice', fontsize=20)
            plt.show()
            flag = False
            continue
            
            
        # If user input is unacceptable    
        except ValueError:
            logging.debug('The number of dice chosen must'\
                ' be a positive integer')
            

dice_distribution()