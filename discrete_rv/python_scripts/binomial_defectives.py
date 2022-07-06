import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s -'\
    ' %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of Program')


def compare_simulated_and_theoretical():
    """This function builds both the simulated and theoretical 
distributions for a binomial random variable modeling the chance of
observing a certain number of successes (we will call them defectives)
in samples of size 'n', with probability of success being 'p'. Users
will choose the parameters 'n' and 'p', as well as the number of samples,
'N'."""
    
    
    # Taking user input for sample size n
    flag = True
    while flag:
        
        
        n_input = input('How large of a sample should we pull from'\
            ' the population of devices? We need an integer of 1 or greater.'\
            ' Or press return to exit: ')
        
        
        # If user wishes to exit
        if not n_input:
            return 'Goodbye'
        
        
        # If user wishes not to exit
        try:
            n = int(n_input)
            if n < 1:
                logging.debug('We need to pull a sample size of 1 or greater.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('We need a positive integer')
            continue
            
    
    # Taking user input for probability of success p
    flag = True
    while flag:
        
        
        p_input = input('What proportion of the population of these'\
            ' devices is defective? Choose a decimal number between 0 and 1'\
            ' Or press return to exit: ')
        
        
        # If user wishes to exit
        if not p_input:
            return 'Goodbye'
        
        
        # If user wishes not to exit
        try:
            p = float(p_input)
            if p < 0 or p > 1:
                logging.debug('We need a decimal number between 0 and 1.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('We need a decimal number between 0 and 1.')
            continue
            
    
    # Taking user input for number of samples N
    flag = True
    while flag:
        
        
        N_input = input('How many samples should we take from the'\
            ' population? We need an integer of 1 or greater.'\
            ' Or press return to exit: ')
        
        
        # If user wishes to exit
        if not N_input:
            return 'Goodbye'
        
        
        # If user wishes not to exit
        try:
            N = int(N_input)
            if N < 1: 
                logging.debug('We need an integer of 1 or greater.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('We need an integer of 1 or greater.')
            continue
    
    
    # Building the Simulated Distribution with our user input
    Z = np.random.choice([1, 0], size=(N, n), p=(p, 1-p))
    Z_values_sim = np.arange(0, n+2)
    Z_success_counts_per_sample = Z.sum(axis=1)

    
    # Building the Theoretical Distribution
    Z_BINS = stats.binom(n, p)
    Z_values_theory = np.arange(0, n+1)
    Z_dist = Z_BINS.pmf(Z_values_theory)

    
    # Reformatting the theoretical probabilities to suppress
    # scientific notation
    Z_dist_formatted = []
    for proportion in Z_dist:
        Z_dist_formatted.append(format(proportion, '.6f'))
    Z_dist_series = pd.Series(Z_dist_formatted)

    
    # Converting the counts from the simulated data to 
    # probabilities, so that we may directly compare with probabilities
    # generated through the theoretical method
    Z_success_series = pd.Series(Z_success_counts_per_sample)
    Z_success_series_prop = Z_success_series.value_counts()/Z.shape[0]
    Z_probabilities = Z_success_series_prop.sort_index()

    
    # Comparing the two lists of probabilities
    print(f'We have simulated probabilities:\n{Z_probabilities}\n\n'\
        f'and we havetheoretical probabilities:\n{Z_dist_series}')

    
    # Visually comparing the two distributions
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(Z_success_counts_per_sample,\
        Z_values_sim, ec='k', alpha=0.2, label='Simulated', density=True)
    ax.scatter(Z_values_theory, Z_dist, c='r', label='Theoretical')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Possible Number of Defectives per Sample', fontsize=20)
    plt.ylabel('P(Number of Defective in a Given Sample)',\
        fontsize=20)
    plt.legend(prop={'size': 20})
    fig.suptitle(f'Probability of Number of Defectives in Samples of Size {n}',\
        fontsize=20)
    plt.show()
    

compare_simulated_and_theoretical()