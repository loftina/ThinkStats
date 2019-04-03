import random
import myplot
import Cdf


def main():
    # Exercise 4.1
    mean = 32.6
    lambd = 1 / mean     # l for lambda
    exp_values = []
    for _ in range(44):
        exp_values.append(random.expovariate(lambd))

    exponential_distribution_cdf = Cdf.MakeCdfFromList(exp_values, name='Exponential Distribution')

    myplot.Cdf(exponential_distribution_cdf, complement=True, xscale='linear', yscale='log')
    myplot.show()

    # Exercise 4.2
    # no.


if __name__ == '__main__':
    main()
