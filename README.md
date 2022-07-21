# Statistics Teaching Tools

Programs for learning entry-level statistics

Following is a breakdown of the different directories and their contents. Relevant python scripts, sql and database files, csv files, etc. can be located within separate directories within each section. 

<b> cards </b>
1. python_scripts
    1. deck_cards_binomial_rv_cumulative_prob.py 
        1. A program that models a random variable, X, following a binomial distribution constructed within the program. Users choose the size of the draw, n cards, from a 52-card, standard deck, and they choose the event they wish to observe. The event can be as small as a single card or as large as all 52 cards. Users also choose the number of successes, k, from the event in their draw of n cards, the theoretical probability of which is computed by the program. Finally, a histogram of the constructed distribution is generated, giving users a visual of the cumulative probability from 0 successes up to and including the number of k successes chosen.

<b> games </b>
1. python_scripts
    1. greedy_pig.py
        1. A game in which users gamble whether or not to roll the die again, collecting points so long as the face value of the die is different from 1. Soon as the face value is 1, all points earned in the round are lost.

<b> dice </b>
1. python_scripts
    1. greedy_pig_distribution.py
        1. A program that models the geometric random variable, X, followed by the toss of a die in a game of Greedy Pig, the rules for which are briefly mentioned in the <b>games</b> section.
    2. rolling_x_dice.py
        1. A program that models the binomial random variable, X, followed by the toss of x die (x being determined by the user) 100,000 times.

<b> discrete_rv </b>
1. python_scripts
    1. binomial_defectives.py
        1. A program that simulates what happens when a binomial random variable models the chance of observing defectives, with probability of defective being 'p', in 'N' samples of size 'n'. All variables are chosen by the user. The program will also compare the simulated distribution with the theoretical distribution.

<b> distributions </b>
1. general
    1. python_scripts
        1. p_hat_from_simulated_binom.py
            1. This program compares binomial and p-hat sampling distributions with their theoretical normal counterparts.
2. sports
    1. NBA
        1. steph_curry
            1. p_hat_steph_curry_free_throw_pct.py
            2. steph_curry_game_stats_db_generator.py
            3. sql_db_files
                1. steph_curry_game_stats.db
                2. sqlite_on_steph_curry_game_stata.sql
                3. schema
                    1. mysql_schema_steph_curry_game_stats
            4. raw_steph_curry_game_stats
                1. regular_season_09_10.xls
                2. regular_season_10_11.xls
                3. regular_season_11_12.xls
                4. regular_season_12_13.xls
                5. regular_season_13_14.xls
                6. regular_season_14_15.xls
                7. regular_season_15_16.xls
                8. regular_season_16_17.xls
                9. regular_season_17_18.xls
                10. regular_season_18_19.xls
                11. regular_season_19_20.xls
                12. regular_season_20_21.xls
                13. regular_season_21_22.xls
            5. cleaned_steph_curry_game_stats
                1. season_09_10.csv
                2. season_10_11.csv
                3. season_11_12.csv
                4. season_12_13.csv
                5. season_13_14.csv
                6. season_14_15.csv
                7. season_15_16.csv
                8. season_16_17.csv
                9. season_17_18.csv
                10. season_18_19.csv
                11. season_19_20.csv
                12. season_20_21.csv
                13. season_21_22.csv
                
<b> probability </b>
1. python_scripts
    1. hiphopcandidates
        1. hiphopcandidates.csv
        2. hiphopcandidates.py
        3. hiphopcandidates_probability.py
        4. sql_db_files
            1. hiphopcandidates.db
            2. sqlite_on_hiphopcandidates.sql
            3. schema
                1. artists.csv
                2. candidates.csv
                3. songentries.csv
                4. mysql_schema
                
<b> populaton_vs_sample </b>
1. population_vs_sample.tex

<b> data_types </b>
1. data_types.tex
2. python_scripts
    1. data_types_db_generator.py
    2. players_last_name_h.py
    3. players_last_name_h.xls
    4. players_points_rankings_21_22.py
    5. players_points_rankings_21_22.xls
    6. sql_db_file
        1. players_last_name_h.db
        2. players_points_rankings_21_22.db
        3. sqlite_on_players_last_name_g.sql
        4. sqlite_on_players_points_rankings_21_22.sql
        5. schema
            1. colleges.csv
            2. mysql_schema_players_last_name_h
            3. mysql_schema_players_points_rankings_21_22.sql
            4. players_last_name_h.csv
            5. players_points_rankings_21_22.csv
            6. positions.csv
3. python_generated_tables
    1. players_last_name_h_nominal.tex
    2. players_last_name_h_nominal_interval_ratio.tex
    3. players_points_rankings_21_22_ordinal_nominal_ratio.tex

<b> data </b>
1. csu
    1. students_enrollment
        1. by_ethnicity
            1. python_scripts
                1. csu_enrollment_by_ethnic_origin_03_07.py
                2. csu_enrollment_by_ethnic_origin_08_12.py
                3. sql_db_files
                    1. csu_enrollment_by_ethnic_origin_03_07.db
                    2. csu_enrollment_by_ethnic_origin_03_07.sql
                    3. csu_enrollment_by_ethnic_origin_08_12.db
                    4. csu_enrollment_by_ethnic_origin_08_12.sql
                    5. schema
                        1. mysql_schema_csu_enrollment_by_ethnic_origin_03_07
                        2. mysql_schema_csu_enrollment_by_ethnic_origin_08_12
            2. csu_enrollment_by_ethnic_origin_03_07.pdf
            3. csu_enrollment_by_ethnic_origin_08_12.pdf
            4. csu_enrollment_by_ethnic_origin_13_17.pdf
            5. csu_enrollment_by_ethnic_origin_17_21.pdf