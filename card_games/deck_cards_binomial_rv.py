import numpy as np
import pandas as pd
import scipy.special as sp
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s -'\
    ' %(message)s')


logging.debug('Start of Program')


# We first must build the standard, 52-card deck. Then we must wrap it in a
# pandas Series
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen',\
    'king']
deck = [rank + '_' + suit for rank in ranks for suit in suits]
D = pd.Series(deck)


def binom_deck_params():
    """This function will set up the parameter 'n', which is number of
Bernoulli trials (number of cards drawn in this experiment), 'E', which is
our desired event, and 'k', which is the number of desired successes
on event 'E'."""
    
    
    # User input for parameter 'n'
    flag = True
    while flag:
        
        
        num_cards_drawn_input = input('How many cards would you like to draw'\
            ' (with replacement)? ')
        
        
        # In case user wishes to exit or does not input an integer within
        # the logical range for standard, 52-card decks
        if not num_cards_drawn_input:
            return 'Goodbye'
        try:
            num_cards_drawn = int(num_cards_drawn_input)
            if num_cards_drawn < 1 or num_cards_drawn > 51:
                logging.debug('Must pull at least 1 and no more than 51'\
                    ' cards.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('The number of cards you wish to pull must be an'\
                ' integer.')
            continue
        
        
    # User input for the 'k'        
    flag = True
    while flag:
        
        
        
        num_successes_input = input(f'How many successes in our random draw'\
            f' of {num_cards_drawn} cards from the deck? ')
        
        
        # In case user wishes to exit or does not input an integer within
        # the logical range 
        if not num_successes_input:
            return 'Goodbye'
        try:
            num_successes = int(num_successes_input)
            if num_successes < 0 or num_successes > num_cards_drawn:
                logging.debug('Must have at least 0 and no more than the'\
                    ' number of drawn cards as your number of successes.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('The number of successes must be an integer.')
            continue
    
    
    # Our event 'E', which is a list of DISTINCT members from the 52-card deck
    event = []
    
    
    # User input for 'E'
    flag = True
    while flag:
        
        
        # In case user wishes to
        # input more than 52 cards
        if len(event) > 51:
            logging.debug('We have chosen all the cards.')
            flag = False
            continue
        
        
        card = input('Which cards are considered a success? Or press return'\
            ' to exit: ')
        
        
        # In case user wishes to
        # exit
        if not card:
            if len(event) == 0:
                exit_input = input('Press return, if you wish to exit.'\
                    ' Press any other key followed by the return key'\
                    ' to return to the prompts. ')
                if not exit_input:
                    return 'Goodbye'
                else:
                    continue
            else:
                flag = False
                continue
        
        
        # In case user wishes to
        # input a member not from the 52-card deck
        elif card not in deck:
            logging.debug('That card is not in the deck. Try again.')
            continue
        
        
        elif card in event:
            logging.debug('You have already chosen that card.')
            continue
        event.append(card)
        continue
        
    
    # This returns a call to the function that will construct the distribution
    # for the user
    return binom_deck(D, num_cards_drawn, num_successes, event)


def binom_deck(series, n, k, E):
    """This function computes the cumulative probability of 'x' successes
in 'n' Bernoulli trials of an experiment with probability of success 'p'.
Our value 'x' will follow a discrete, binomial random variable 'X', with
parameters 'n' and 'p', the distribution for which will be computed here
in this function."""
    
    
    # We need to randomly draw 'n' cards from the deck 'series'
    draw = np.random.choice(series, n, replace=True)
    
    
    # We let the user know if their card(s) have been drawn.
    for card in E:
        if card in draw:
            print(f'The {card} has been drawn!')
            
    
    # We establish our probability of success for the event 'p'
    p = len(E)/series.shape[0]
    
    
    # We need to create the list of probabilities along this distribution
    probabilities = [sp.comb(n, i)*p**(i)*(1-p)**(n-i) for i in range(n+1)]
    
    
    # This computes and returns the cumulative probability for our chosen
    # number of successes 'x'
    return f'P(x <= {k}) = {sum(probabilities[:k+1])}'


print(binom_deck_params())