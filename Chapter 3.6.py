import survey
import Cdf
import myplot

def main():
    # Exercise 3.6
    myBirthWeight = 163
    table = survey.Pregnancies()
    table.ReadRecords()

    unfilteredLiveBirthWeights = [(p.birthwgt_lb, p.birthwgt_oz) for p in table.records if p.outcome == 1]
    liveBirthWeights = [lbs * 16 + oz for lbs, oz in unfilteredLiveBirthWeights if type(lbs) == int and type(oz) == int
                        and lbs * 16 + oz <= 200]
    liveBirthWeightsCdf = Cdf.MakeCdfFromList(liveBirthWeights, name="live birth weights")
    print("My birth weight percentile rank (vs all births): %d"
          % (100 * liveBirthWeightsCdf.Prob(myBirthWeight)))

    unfilteredNotFirstLiveBirthWeights = [(p.birthwgt_lb, p.birthwgt_oz) for p in table.records if p.outcome == 1
                                          and p.birthord != 1]
    notFirstLiveBirthWeights = [lbs * 16 + oz for lbs, oz in unfilteredNotFirstLiveBirthWeights if type(lbs) == int
                                and type(oz) == int and lbs * 16 + oz <= 200]
    notFirstLiveBirthWeightsCdf = Cdf.MakeCdfFromList(notFirstLiveBirthWeights, name="not first live birth weights")
    print("My birth weight percentile rank (vs first births): %d"
          % (100 * notFirstLiveBirthWeightsCdf.Prob(myBirthWeight)))

    myplot.Cdf(notFirstLiveBirthWeightsCdf)
    myplot.Show(title="not first live birth weight CDF", xlabel="birth weight oz", ylabel="probability")

    # Exercise 3.7
    #50%

if __name__ == "__main__":
    main()
