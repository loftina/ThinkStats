import survey
import Cdf

def median(cdf):
    return cdf.Value(.5)


def interquartile(cdf):
    return abs(cdf.Value(.25) - cdf.Value(.75))


def main():
    # Exercise 3.11
    table = survey.Pregnancies()
    table.ReadRecords()
    unfilteredLiveBirthWeights = [(p.birthwgt_lb, p.birthwgt_oz) for p in table.records if p.outcome == 1]
    liveBirthWeights = [lbs * 16 + oz for lbs, oz in unfilteredLiveBirthWeights if type(lbs) == int and type(oz) == int
                        and lbs * 16 + oz <= 200]
    liveBirthWeightsCdf = Cdf.MakeCdfFromList(liveBirthWeights, name="live birth weights")
    print('25th: %d 50th: %d 75th: %d interquartile range: %d' % (liveBirthWeightsCdf.Value(.25),
                                                                  median(liveBirthWeightsCdf),
                                                                  liveBirthWeightsCdf.Value(.75),
                                                                  interquartile(liveBirthWeightsCdf)))


if __name__ == "__main__":
    main()
