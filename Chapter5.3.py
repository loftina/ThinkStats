from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random
import Cdf
import myplot


def get_bread(n):
    """returns the heaviest piece of bread drawn from normal distribution
    with mean weight 950g and standard deviation 50g
    """
    mu, sigma = 950, 50
    loaves = np.random.normal(mu, sigma, n)
    return max(loaves)


def main():
    # Exercise 5.6
    sample_size=365
    for n in range(1,6):
        distribution = []
        for _ in range(sample_size):
            distribution.append(get_bread(n))
        print(np.mean(distribution), np.std(distribution))

    found_distribution = []
    for _ in range(sample_size):
        found_distribution.append(int(get_bread(4)))
    print('picking 4 loaves: mu={} sigma={}'.format(np.mean(found_distribution),np.std(found_distribution)))

    expected_distribution = np.random.normal(np.mean(found_distribution), np.std(found_distribution), sample_size)
    myplot.Cdfs(cdfs=(Cdf.MakeCdfFromList(found_distribution), Cdf.MakeCdfFromList(expected_distribution)))
    myplot.show()
    plt.hist(found_distribution, normed=True, bins=20, label='found')
    plt.hist(expected_distribution, normed=True, bins=20, alpha=.75, label='expected')
    plt.ylabel('Probability')
    plt.xlabel('Bread Weight')
    plt.legend()
    plt.show()

    # Exercise 5.7
    men_heights = np.random.normal(loc=178, scale=59.4, size=99999)
    women_heights = np.random.normal(loc=163, scale=52.8, size=99999)
    pairs = zip(men_heights, women_heights)
    l = [w>m for m, w in pairs]
    print('In {}% of the pairs the woman will be taller than the man'.format(sum(l)/len(l)*100.0))




if __name__ == '__main__':
    main()
