import random
import myplot
import Cdf


def main():
    # Exercise 4.3
    # function defined below
    random_pareto_sample = []
    for i in range(1000):
        random_pareto_sample.append(paretovariate(1, .5))
    random_pareto_sample_cdf = Cdf.MakeCdfFromList(random_pareto_sample)
    myplot.Cdf(random_pareto_sample_cdf, complement=True, xscale='log', yscale='log')
    myplot.show()


    # Exercise 4.4
    heights = []
    for _ in range(6000000000):
        heights.append(paretovariate(alpha=1.7, x_sub_m=100))
    heights_cdf = Cdf.MakeCdfFromList(heights)
    print(heights.Mean())
    print(heights.Percentile(heights.Mean()))
    print(heights.sort())


def paretovariate(alpha, x_sub_m=1):
    return x_sub_m * random.paretovariate(alpha=alpha)


if __name__ == '__main__':
    main()
