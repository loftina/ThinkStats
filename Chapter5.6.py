from __future__ import division
import random
import numpy as np


def get_random(range):
    return int(random.random() * range)


def monte_carlo_chance_of_10_streak(num_of_games):
    average_across_games = 0
    for _ in range(num_of_games):
        made_10_shots = 0
        for _ in range(10):
            # 1 for make, 0 for miss
            shots = [get_random(2) for _ in range(15)]
            shots_string = ''.join(str(shot) for shot in shots)
            if '1'*10 in shots_string:
                made_10_shots+= 1
        # /10games*100 to get percent abreviated to *10
        average_across_games += made_10_shots*10
    return average_across_games/num_of_games


def monte_carlo_cancer(num_of_cohorts):
    average_across_cohorts = 0
    for _ in range(num_of_cohorts):
        positives = 0
        sample_size = 100
        for _ in range(10):
            has_cancer = [random.randrange(0, 1000) == 1 for _ in range(sample_size)]
            positives += sum(has_cancer)
            sample_size -= sum(has_cancer)
        average_across_cohorts += positives/sample_size
    return average_across_cohorts/num_of_cohorts


def main():
    # Exercise 5.11
    #print('{}% chance of 10 shot streak in 1 game.'.format(monte_carlo_chance_of_10_streak(1)))
    #print('{}% chance of 10 shot streak in 82 games.'.format(monte_carlo_chance_of_10_streak(82)))

    # Exercise 5.13
    # 1
    print('{} diagnosed with particular cancer out of 100 patients followed for 10 years!'.format(monte_carlo_cancer(1)))
    print('{} diagnosed with particular cancer out of 100000 patients followed for 10 years!'.format(monte_carlo_cancer(1000)))
    # 2
    # 5 or less positives across 100 patients results in p-value less than 5%
    # 3
    num_cohorts = 100
    has_positive = 0
    for _ in range(num_cohorts):
        positives = 0
        sample_size = 100
        for _ in range(10):
            has_cancer = [random.randrange(0, 1000) == 1 for _ in range(100)] # 100 patients per cohort
            positives += sum(has_cancer)
            sample_size -= sum(has_cancer)
        if positives >= 1:
            has_positive += 1
    odds_of_significant_cluster = has_positive/num_cohorts
    #print('Chance that at least 1/100 cohorts of 100 patients has p-value >= 1%: {}'.format(odds_of_significant_cluster))
    # 4
    # assuming alpha of .01

    population_matrix = []
    for _ in range(100):# creating 100 rows
        has_cancer = [random.randrange(0, 1000) == 1 for _ in range(100)] # following 100 patients for a year
        for _ in range(9): # loop to simulate 9 additional years
            for patient in range(len(has_cancer)):
                if has_cancer[patient] == False:
                    has_cancer[patient] = random.randrange(0,1000) == 1
        population_matrix.append(has_cancer)

    num_groups = 0
    significant_clusters = 0
    for row in range(len(population_matrix)-9):
        for column in range(len(population_matrix)-9):
            num_groups += 1
            current_group = []
            for group_size in range(10):
                current_group.append(population_matrix[row+group_size][column:column+9])
            found = False
            while not found:
                for subgroup in current_group:
                    if True in subgroup:
                        found = True
                if found:
                    significant_clusters += 1
                found = True
    print(significant_clusters/num_groups)
    # 5








if __name__ == '__main__':
    main()
