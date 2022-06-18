import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pandas as pd
import scipy.stats as stats
import numpy as np
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s'\
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of Program')


import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pandas as pd
import scipy.stats as stats
import numpy as np
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s'\
    ' - %(message)s')
logging.getLogger('matplotlib.fontmanager').disabled = True


logging.debug('hello')


def binomial_to_p_hat():
    
    
    # User input for sample size n
    flag = True
    while flag:
        
        
        n_input = input('Choose your sample size. Value must be a'\
            ' positive integer. Or press return to exit: ')
        
        
        if not n_input:
            return 'Goodbye'
        
        
        try:
            n = int(n_input)
            if n < 1:
                logging.debug('Sample size must be a positive integer.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Sample size must be a positive integer.')
            continue
            
            
    # User input for probability of success p
    flag = True
    while flag:
        
        
        p_input = input('Choose your probability of success.'\
            ' Value must be a number in the interval [0, 1].'\
            ' Or press return to exit: ')
        
        
        if not p_input:
            return 'Goodbye'
        
        
        try:
            p = float(p_input)
            if p < 0 or p > 1:
                logging.debug('Value must be a number in the interval [0, 1].')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Value must be a number in the interval [0, 1].')
            continue
            
            
    # Display theoretical mean and standard deviation of the 
    # probability distribution with parameters 'n' and 'p'
    print('\n\n')
    print(f'The mean: {n*p}')
    print('\n')
    print(f'The standard deviation: {np.sqrt(n*p*(1-p))}')
    print('\n\n')
    
    
    # User input for lower bound for area under the curve
    flag = True
    while flag:
        
        
        lower_input = input('Choose your lower bound for'\
            ' area under the curve. Value must be and integer'\
            f' in the interval [0, {n}].'\
            ' Or press return to exit: ')
        
        
        if not lower_input:
            return 'Goodbye'
        
        
        try:
            lower = int(lower_input)
            if lower < 0 or lower > n:
                logging.debug('Value must be and integer in [0, {n}].')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Value must be an integer in [0, {n}].')
            continue
            
            
    # User input for upper bound for area under the curve
    flag = True
    while flag:
        
        
        upper_input = input('Choose your upper bound for'\
            ' area under the curve. Value must be an integer'\
            f' in the interval [{lower}, {n}].'\
            ' Or press return to exit: ')
        
        
        if not upper_input:
            return 'Goodbye'
        
        
        try:
            upper = int(upper_input)
            if upper < lower or upper > n:
                logging.debug('Value must be an integer in'\
                    ' [{lower}, {n}].')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Value must be an integer in [{lower}, {n}].')
            continue
            
            
    print('\n\n')
            
            
    # Theoretical Binomial Distribution
    X = stats.binom(n, p)
    X_domain = np.arange(0, n+1)
    X_rv = X.pmf(X_domain)
    

    # Taking 1 million samples from the Theoretical Binomial 
    # Distribution of 'n' trials of a chance outcome with 
    # probability of success 'p'.
    X_samples = X.rvs(10**6)
    print(X_samples)
    print(f'Probability for the binomial outcome in interval'\
        f' [{lower}, {upper}]:'\
        f' {((X_samples>=lower) & (X_samples<=upper)).sum()/(10**6)}\n')
    

    # Theoretical Normal Distribution having mean and standard deviation
    # equal to their respective counterparts in the theoretical
    # binomial distribution
    Y = stats.norm(X.mean(), X.std())
    Y_domain = np.linspace(0, n, 1000)
    def pdf_values(X, x):
        return X.pdf(x)
    Y_rv = pdf_values(Y, Y_domain)


    # Taking 1 million samples from the Theoretical Normal 
    # Distribution mean and standard deviation
    # equal to their respective counterparts in the theoretical
    # binomial distribution
    Y_samples = Y.rvs(10**6)
    print(f'Probability for the normal outcome in interval'\
        f' ({lower}, {upper}):'\
        f' {((Y_samples>lower) & (Y_samples<upper)).sum()/(10**6)}\n')

    
    # Plotting
    bins = list(range(n+1))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(X_samples, bins=bins, ec='k', alpha=0.3, density=True)
    ax.plot(Y_domain, Y_rv)
    plt.ylim(0, Y_rv.max()+(Y_rv.max()/10**2))
    ix = np.linspace(lower, upper, 1000)
    iy = pdf_values(Y, ix)
    verts = [(lower, 0), *zip(ix, iy), (upper, 0)]
    poly = Polygon(verts, facecolor='0.15', edgecolor='0', alpha=0.7)
    ax.add_patch(poly)
    plt.show()
    
    
    # We have the probability, p_avg, of observing a value between the
    # 'lower' and 'upper' bounds input by the user.
    # This will serve as our probability of success in the 
    # distribution of p-hats we construct.
    p_avg = ((X_samples>=lower) & (X_samples<=upper)).sum()/(10**6)

    
    # Now we construct our p-hat distribution
    
    
    # User input for sample size, m, to be pulled from the binomial
    # distribution followed by random variable X above
    flag = True
    while flag:
        
        
        m_input = input('Choose your sample size. Value must be a'\
            ' positive integer. Or press return to exit: ')
        
        
        if not m_input:
            return 'Goodbye'
        
        
        try:
            m = int(m_input)
            if m < 1:
                logging.debug('Sample size must be a positive integer.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Sample size must be a positive integer.')
            continue
            
            
    # User input for number of samples N
    flag = True
    while flag:
        
        
        N_input = input('Choose the number of samples. Value must be a'\
            ' positive integer. Or press return to exit: ')
        
        
        if not N_input:
            return 'Goodbye'
        
        
        try:
            N = int(N_input)
            if N < 1:
                logging.debug('Number of samples must be a positive integer.')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Number of samples must be a positive integer.')
            continue
            
    
    # The list of N p-hats resulting from N experiments, each of 
    # size m
    p_hats = np.empty(shape=(1, N))
    for i in range(N):
        sample = X.rvs(m)
        successes = []
        for j in sample:
            if j >= lower and j <= upper:
                successes.append(j)
        p_hats[0][i] = len(successes)/m
    
    
    # Constructing the histogram and normal distribution
    mean_p_hat = p_avg
    std_p_hat = np.sqrt(p_avg*(1-p_avg)/m)
    increment = (p_hats.max() - p_hats.min())/10
    low_bins = p_hats.min()
    upp_bins = p_hats.max() + increment
    bins = np.arange(low_bins, upp_bins, increment)
    print('\n')
    print(p_hats)
    print('\n')
    print(p_hats.max())
    print('\n')
    print(p_hats.min())
    print('\n')
    print('done')
    #bin_num = int(np.ceil(m/10))
    #print(bin_num)
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(p_hats[0], bins=bins.tolist(), ec='k', density=True)
    Y = stats.norm(mean_p_hat, std_p_hat)
    u = np.linspace(p_hats.min(), p_hats.max(), 1000)
    ax.plot(u, Y.pdf(u))
    plt.show()
    
    
    
binomial_to_p_hat()

