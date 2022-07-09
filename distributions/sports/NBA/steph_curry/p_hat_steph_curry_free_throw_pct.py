import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s'\
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of Program')


# Below, wrapped in a pandas Series, is the population of Stephen Curry's
# Free Throw percentage per game.
# We can construct a p-hat distribution with this population data.


def p_hat_distribution(sc_career):
    """This function populates the population of Steph Curry's per-game
Free Throw Percentage (FT%) onto a histogram, then it pulls a number of samples,
number and sample size determined by user input, from that population
distribution, computing for each sample the proportion (p-hat) of those
exhibiting a percentage greater than or equal to the mean of the population.
Because we expect the Sampling Distribution of p-hats to approximate a normal
distribution, we overlay the Theoretical Normal Distribution, with those
parameters of the Sampling Distribution of p-hats, within the same figure
for a comparison."""
    
    
    # We check that all values are real numbers
    print(f'We have a population containing {sc_career.shape[0]} specimen.')
    print(f'We have {sc_career.map(np.isreal).sum()} real values in our'\
        ' popultion')


    # We have 720 specimen in this population. Below, so that we may begin to
    # construct a p-hat, we get the mean of the
    # population.
    print(f'The distribution of our population has a mean of'\
        f' {sc_career.mean()}')


    # The shape of the population distribution is strongly left-skewed, as seen
    # below.


    # We increment across the range of values to create our histogram bins
    increment = (sc_career.max() - sc_career.min())/10
    bins = list(np.arange(sc_career.min(), sc_career.max()+increment,\
        increment))
    
    
    # We plot the histogram
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(sc_career.tolist(), bins=bins, ec='k',\
        label='Mean (mu):' + r' $\mu = 0.89717$')
    plt.xlabel('FT% per Game', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    fig.suptitle('Population: Steph Curry Free Throw Percentage (FT%)'\
        ' per Game', fontsize=20)
    plt.legend(prop={'size': 20})
    plt.show()


    # We begin constructing out p-hat distribution.
    # We will satisfy the Large Counts Condition with 5 (instead of 10) as the 
    # lower bound, for samples of size between 49 and 71, which is less than
    # 10% of 720.
    
    
    # We take user input for the sample size.
    flag = True
    while flag:
        
        
        n_input = input('Choose a sample size. You must choose an integer'\
            ' between 49 and 71, or press return to exit.')
        
        
        # If the user wishes to exit
        if not n_input:
            return 'Goodbye'
        
        
        # If the user wishes not to exit
        try:
            n = int(n_input)
            if n < 49 or n > 71:
                logging.debug('Must choose an integer between 49 and 71')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('Must choose an integer between 49 and 71')
            continue
    
    
    # We collect user input for the number of samples
    flag = True
    while flag:
        
        
        N_input = input('Choose the number of samples you would like to pull.'\
            ' You must choose a positive integer no greater than 1000,'\
            ' or press return to exit.')
        
        
        # If the user wishes to exit
        if not N_input:
            return 'Goodbye'
        
        
        # If the user does not wish to exit
        try:
            N = int(N_input)
            if N < 1 or N > 1000:
                logging.debug('must choose a positive integer no greater than'\
                    ' 1000')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('must choose a positive integer no greater than'\
                    ' 1000')
            continue
    
    
    # We have the mean of our population distribution
    mu = sc_career.mean()
    
    
    # We have the probability of pulling a specimen, with value greater than
    # or equal to the mean, from the population
    p = (sc_career >= sc_career.mean()).sum()/sc_career.shape[0]
    
    
    # Here we print out the probability of pulling a single game exhibiting
    # a Free Throw Percentage greater than or equal to Steph Curry's FT%
    print(f'If random variable X follows the population distribution, then'\
        ' the probability of pulling a specimen from the population with value'\
        f' greater than or equal to the mean, mu={mu}, is'\
        f' {np.round(p, 2)}')
    
    
    # We pull our samples of size 'n' from the population an compute, for each
    # sample, the resulting p-hat
    p_hats = []
    for i in range(N):
        sample = np.random.choice(sc_career, size=n, replace=False)
        successes = []
        for j in sample:
            if j >= sc_career.mean():
                successes.append(j)
        p_hats.append(len(successes)/n)
    
    
    # We construct the bins for the histogram of our p-hat distribution
    lower_bins = min(p_hats)
    upper_bins = max(p_hats)
    increment = (upper_bins - lower_bins)/10
    bins = np.arange(lower_bins, upper_bins + increment, increment)
    
    
    # We construct the normal distribution that our p-hat distribution
    # approximates
    p_avg = p
    p_std_dev = np.sqrt(p_avg*(1-p_avg)/n)
    Y = stats.norm(p_avg, p_std_dev)
    Y_domain = np.linspace(-1, 2, 1000)
    Y_freq = Y.pdf(Y_domain)
    
    
    # Now we plot our graph
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(p_hats, bins=bins, ec='k', density=True,\
        label='Sampling Distribution of p_hat')
    ax.plot(Y_domain, Y_freq,\
        label=f'N({np.round(p_avg, 2)}, {np.round(p_std_dev, 2)})')
    plt.xlim(p_avg-(6*p_std_dev), p_avg+(6*p_std_dev))
    plt.xlabel('Proportion of Games with FT% Greater or Equal to mu',\
        fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(prop={'size': 10})
    fig.suptitle('Sampling Distribution of Proportion of Games with FT%'\
        f' Greater or Equal to mu', fontsize=20)
    plt.show()


# We can observe, via the Law of Large Numbers, the behavior of the average
# number of successes in N Bernoulli trials, each with a probability of success
# matching Steph Curry's Free Throw percentage success.


def free_throw_avg_behavior():
    """This function tracks the behavior of N Bernoulli trials with probability
of success equal to Steph Curry's FT%. The number of trials, N, will be input
by the user."""

    
    # We take user input for the number, N, of Bernoulli trials
    flag = True
    while flag:
        
        
        N_input = input('How many Free Throws? Choose a positive integer'\
            ' no greater than 10 thousand, or press return to exit.')
        
        
        # If the user wishes to exit
        if not N_input:
            return 'Goodbye'
        
        
        # If the user wishes not to exit
        try:
            N = int(N_input)
            if N < 1 or N > 10000:
                logging.debug('We need a positive integer no greater than'\
                    ' 10000')
                continue
            flag = False
            continue
        except ValueError:
            logging.debug('We need a positive integer no greater than 10000')
            continue
    
    
    # Here we collect members of our domain, 'trials', and members of our
    # range, 'avgs'
    s = 0
    trials = []
    avgs = []
    for i in range(1, N+1):
        result = np.random.choice([1, 0], size=1, p=(sc_career.mean(),\
            1-sc_career.mean()))
        if result == 1:
            s += 1
        trials.append(i)
        avgs.append(float(s/i))
        
        
    # Finally, we plot the figure
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.plot(trials, avgs, label='FT%')
    ax.axhline(y=sc_career.mean(), c='k', linestyle='--',\
        label='Theoretical Average')
    plt.xlabel('Number of Free Throws', fontsize=20)
    plt.ylabel('FT%', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    fig.suptitle(f'FT% as Function of Number of Free Throws with success'\
        f' p={np.round(sc_career.mean(), 5)}', fontsize=20)
    plt.legend(prop={'size': 20})
    plt.show()


# Following are per-game, regular season stats for Steph Curry, across all
# regular seasons. We will focus on Free Throw Percentage (FT%).
# We will construct pandas Series, each containing a single season's FT%
# per game.


# Season 2009-2010
df_09 = pd.read_csv('cleaned_steph_curry_game_stats/season_09_10.csv')
sc_09 = df_09.loc[df_09['free_throw_pct'].notnull()]


# Season 2010-2011
df_10 = pd.read_csv('cleaned_steph_curry_game_stats/season_10_11.csv')
sc_10 = df_10.loc[df_10['free_throw_pct'].notnull()]


# Season 2011-2012
df_11 = pd.read_csv('cleaned_steph_curry_game_stats/season_11_12.csv')
sc_11 = df_11.loc[df_11['free_throw_pct'].notnull()]


# Season 2012-2013
df_12 = pd.read_csv('cleaned_steph_curry_game_stats/season_12_13.csv')
sc_12 = df_12.loc[df_12['free_throw_pct'].notnull()]


# Season 2013-2014
df_13 = pd.read_csv('cleaned_steph_curry_game_stats/season_13_14.csv')
sc_13 = df_13.loc[df_13['free_throw_pct'].notnull()]


# Season 2014-2015
df_14 = pd.read_csv('cleaned_steph_curry_game_stats/season_14_15.csv')
sc_14 = df_14.loc[df_14['free_throw_pct'].notnull()]


# Season 2015-2016
df_15 = pd.read_csv('cleaned_steph_curry_game_stats/season_15_16.csv')
sc_15 = df_15.loc[df_15['free_throw_pct'].notnull()]


# Season 2016-2017
df_16 = pd.read_csv('cleaned_steph_curry_game_stats/season_16_17.csv')
sc_16 = df_16.loc[df_16['free_throw_pct'].notnull()]


# Season 2017-2018
df_17 = pd.read_csv('cleaned_steph_curry_game_stats/season_17_18.csv')
sc_17 = df_17.loc[df_17['free_throw_pct'].notnull()]


# Season 2018-2019
df_18 = pd.read_csv('cleaned_steph_curry_game_stats/season_18_19.csv')
sc_18 = df_18.loc[df_18['free_throw_pct'].notnull()]


# Season 2019-2020
df_19 = pd.read_csv('cleaned_steph_curry_game_stats/season_19_20.csv')
sc_19 = df_19.loc[df_19['free_throw_pct'].notnull()]


# Season 2020-2021
df_20 = pd.read_csv('cleaned_steph_curry_game_stats/season_20_21.csv')
sc_20 = df_20.loc[df_20['free_throw_pct'].notnull()]


# Season 2021-2022
df_21 = pd.read_csv('cleaned_steph_curry_game_stats/season_21_22.csv')
sc_21 = df_21.loc[df_21['free_throw_pct'].notnull()]


sc_career = pd.concat(
    [
        sc_09['free_throw_pct'],
        sc_10['free_throw_pct'],
        sc_11['free_throw_pct'],
        sc_12['free_throw_pct'],
        sc_13['free_throw_pct'],
        sc_14['free_throw_pct'],
        sc_15['free_throw_pct'],
        sc_16['free_throw_pct'],
        sc_17['free_throw_pct'],
        sc_18['free_throw_pct'],
        sc_19['free_throw_pct'],
        sc_20['free_throw_pct'],
        sc_21['free_throw_pct']
    ]
)


p_hat_distribution(sc_career)


free_throw_avg_behavior()