import random
import Cdf
import Pmf
import myplot
import survey


def sample(cdf, n):
    return [cdf.Random() for x in range(n)]


def main():
    # Exercise 3.9
    table = survey.Pregnancies()
    table.ReadRecords()
    unfilteredLiveBirthWeights = [(p.birthwgt_lb, p.birthwgt_oz) for p in table.records if p.outcome == 1]
    liveBirthWeights = [lbs * 16 + oz for lbs, oz in unfilteredLiveBirthWeights if type(lbs) == int and type(oz) == int
                        and lbs * 16 + oz <= 200]
    liveBirthWeightsCdf = Cdf.MakeCdfFromList(liveBirthWeights, name="live birth weights")
    samepleListLiveBirthWeights = sample(liveBirthWeightsCdf, 1000)
    myplot.Cdf(Cdf.MakeCdfFromList(samepleListLiveBirthWeights))
    myplot.show(title="CDF of live births resampled")

    # Exercise 3.10
    randomList = [random.random() for x in range(1000)]
    myplot.Pmf(Pmf.MakePmfFromList(randomList))
    myplot.show(title="random pmf")
    myplot.Cdf(Cdf.MakeCdfFromList(randomList))
    myplot.Show(title="random cdf")


if __name__ == "__main__":
    main()
