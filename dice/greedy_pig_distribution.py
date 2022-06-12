import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of Program')


def greedy_pig_roll_count(roll=1):
    """This function will roll the die and tally the number of rolls
    until a face value of 1 is observed, at which point, the function
    adds one final count to the tally before returning that tally."""
    
    
    # We build the die for this game and start our count at 0
    faces = np.arange(1, 7)
    count = 0
    
    
    
    flag = True
    while flag:
        
        
        # We roll the die and determine whether or not its
        # face value is a 1, counting every roll along the way
        face = np.random.choice(faces, roll)
        if face == 1:
            count += 1
            flag = False
            continue
        count += 1
        
        
    return count


def greedy_pig_distribution(games=10000):
    """This function will call on the greedy_pig_roll_counts function
    some number of times, x, determined by the user, and return a list of 
    counts produced by x calls to the greedy_pig_roll_count function."""
    
    
    # Here is where we generate our list of counts
    counts = []
    for i in list(range(games)):
        counts.append(greedy_pig_roll_count())
        
        
    return counts


# Here, we collect user input
flag = True
while flag:
    
    
    
    games_input = input('How many games? ')
    
    
    # If users wish not to continue
    if not games_input:
        print('Goodbye')
        flag = False
        continue
        
        
    # If users wish to continue
    try:
        games = int(games_input)
        # We take our user input, in the 'games' variable, and
        # use it to construct our distribution
        rolls_per_game = greedy_pig_distribution(games)


        # We create a pandas series with our list of counts from
        # the greedy_pig_distribution function
        rolls_per_game_series = pd.Series(rolls_per_game)


        # We get the count on each distinct count and sort those values
        sorted_rolls_per_game_series = rolls_per_game_series.value_counts().sort_index()


        # Finally, we construct the plot of the distribution
        sorted_rolls_per_game_series.plot(kind='bar', figsize=(15, 10))
        plt.xlabel('Rolls per Game', fontsize=20)
        plt.ylabel('Count of Rolls per Game', fontsize=20)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.suptitle('Greed Pig Distribution', fontsize=20)
        plt.show()
        
        
        flag = False
        continue
        
        
    # If users fail to input an integer    
    except ValueError:
        logging.debug('Must be a positive integer')
        continue
        

