import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s'\
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of Program')


# Below, wrapped in a pandas Series, is the population of Stephen Curry's
# Free Throw percentage per game.
# We can construct a p-hat distribution with this population data.


def p_hat_distribution(sc_career):
    
    
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
    ax.hist(sc_career.tolist(), bins=bins, ec='k')
    plt.show()


    # We will get Large Counts Condition with 5 (instead of 10) as the lower
    # bound, for samples of size between 49 and 71, which is less than 10% of
    # 720.
    
    
    flag = True
    while flag:
        
        
        n_input = input('Choose a sample size. You must choose an integer'\
            ' between 49 and 71, or press return to exit.')
        
        
        if not n_input:
            return 'Goodbye'
        
        
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
    
    
    flag = True
    while flag:
        
        
        N_input = input('Choose the number of samples you would like to pull.'\
            ' You must choose a positive integer no greater than 1000,'\
            ' or press return to exit.')
        
        
        if not N_input:
            return 'Goodbye'
        
        
        try:
            N = int(N_input)
            if n < 1 or n > 1000:
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
    
    
    print(f'If random variable X follows the population distribution, then'\
        ' the probability of pulling a specimen from the population with value'\
        f' greater than or equal to the mean, mu={mu}, is'\
        f' P(X >= mu) = {p}')
    
    
    # We pull our samples of size 'n' from the population
    p_hats = []
    for i in range(N):
        sample = np.random.choice(sc_career, size=n, replace=False)
        successes = []
        for j in sample:
            if j >= sc_career.mean():
                successes.append(j)
        p_hats.append(len(successes)/n)
    print(p_hats)
    
    
    lower_bins = min(p_hats)
    upper_bins = max(p_hats)
    increment = (upper_bins - lower_bins)/10
    bins = np.arange(lower_bins, upper_bins + increment, increment)
    
    
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.hist(p_hats, bins=bins, ec='k', density=True)
    plt.show()


# We can observe, via the Law of Large Numbers, the behavior of the average
# number of successes in N Bernoulli trials, each with a probability of success
# matching Steph Curry's Free Throw percentage success.


def free_throw_avg_behavior():


    N = 200
    s = 0
    trials = []
    avgs = []
    for i in range(1, N+1):
        result = np.random.choice([1, 0], size=1, p=(sc_career.mean(), 1-sc_career.mean()))
        if result == 1:
            s += 1
        trials.append(i)
        avgs.append(float(s/i))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.plot(trials, avgs)
    ax.axhline(y=sc_career.mean(), c='k', linestyle='--')
    plt.show()


# Following are per-game, regular season stats for Steph Curry, across all
# regular seasons. We will focus on Free Throw Percentage (FT%).
# We will construct pandas Series, each containing a single season's FT%
# per game.


# REGULAR SEASON 09 FT%


sc_09 = pd.read_excel('steph_curry_game_stats/regular_season_09_10.xls')
sc_09 = sc_09.loc[sc_09['FT%'].notnull()]
sc_09.drop([66, 67], inplace=True)


# REGULAR SEASON 10 FT%


sc_10 = pd.read_excel('steph_curry_game_stats/regular_season_10_11.xls')
sc_10 = sc_10.loc[sc_10['FT%'].notnull()]
sc_10.drop([2, 3, 22, 23, 24, 25, 26, 27], inplace=True)


# REGULAR SEASON 11 FT%


sc_11 = pd.read_excel('steph_curry_game_stats/regular_season_11_12.xls')
sc_11 = sc_11.loc[sc_11['FT%'].notnull()]
sc_11.drop([2, 6, 7, 8, 9, 10, 11, 12, 13], inplace=True)
sc_11 = sc_11.loc[:29]


# REGULAR SEASON 12 FT%


sc_12 = pd.read_excel('steph_curry_game_stats/regular_season_12_13.xls')
sc_12 = sc_12.loc[sc_12['FT%'].notnull()]
sc_12.drop([36, 37, 44, 45], inplace=True)


# REGULAR SEASON 13 FT%


sc_13 = pd.read_excel('steph_curry_game_stats/regular_season_13_14.xls')
sc_13 = sc_13.loc[sc_13['FT%'].notnull()]
sc_13.drop([5, 11, 12, 81], inplace=True)


# REGULAR SEASON 14 FT%


sc_14 = pd.read_excel('steph_curry_game_stats/regular_season_14_15.xls')
sc_14 = sc_14.loc[sc_14['FT%'].notnull()]
sc_14.drop([52, 63], inplace=True)


# REGULAR SEASON 15 FT%


sc_15 = pd.read_excel('steph_curry_game_stats/regular_season_15_16.xls')
sc_15 = sc_15.loc[sc_15['FT%'].notnull()]
sc_15.drop([30, 31, 58], inplace=True)


# REGULAR SEASON 16 FT%


sc_16 = pd.read_excel('steph_curry_game_stats/regular_season_16_17.xls')
sc_16 = sc_16.loc[sc_16['FT%'].notnull()]
sc_16.drop([47, 65, 79], inplace=True)


# REGULAR SEASON 17 FT%


sc_17 = pd.read_excel('steph_curry_game_stats/regular_season_17_18.xls')
sc_17 = sc_17.loc[sc_17['FT%'].notnull()]
sc_17.drop([13, 20, 41, 42], inplace=True)
sc_17 = pd.concat([sc_17.loc[:24], sc_17.loc[36:64], sc_17.loc[71:71]], axis=0)


# REGULAR SEASON 18 FT%


sc_18 = pd.read_excel('steph_curry_game_stats/regular_season_18_19.xls')
sc_18 = sc_18.loc[sc_18['FT%'].notnull()]
sc_18.drop([71, 81], inplace=True)
sc_18 = pd.concat([sc_18.loc[:10], sc_18.loc[23:]], axis=0)


# REGULAR SEASON 19 FT%


sc_19 = pd.read_excel('steph_curry_game_stats/regular_season_19_20.xls')
sc_19 = sc_19.loc[sc_19['FT%'].notnull()]
sc_19 = pd.concat([sc_19.loc[:3], sc_19.loc[62:62]], axis=0)


# REGULAR SEASON 20 FT%


sc_20 = pd.read_excel('steph_curry_game_stats/regular_season_20_21.xls')
sc_20 = sc_20.loc[sc_20['FT%'].notnull()]
sc_20.drop([30, 36, 41, 42, 43, 44, 45, 48, 70], inplace=True)


# REGULAR SEASON 21 FT%


sc_21 = pd.read_excel('steph_curry_game_stats/regular_season_21_22.xls')
sc_21 = sc_21.loc[sc_21['FT%'].notnull()]
sc_21.drop([15, 29, 37, 42, 51, 64], inplace=True)
sc_21 = sc_18.loc[:68]


# REGULAR SEASON CAREER FT%


sc_career = pd.concat(
    [
        sc_09['FT%'],
        sc_10['FT%'],
        sc_11['FT%'],
        sc_12['FT%'],
        sc_13['FT%'],
        sc_14['FT%'],
        sc_15['FT%'],
        sc_16['FT%'],
        sc_17['FT%'],
        sc_18['FT%'],
        sc_19['FT%'],
        sc_20['FT%'],
        sc_21['FT%']
    ]
)


p_hat_distribution(sc_career)


free_throw_avg_behavior()

