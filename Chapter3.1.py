import Pmf
import matplotlib.pyplot as plt
from operator import itemgetter
import relay
import myplot


def UnbiasPmf(pmf, name):
    unbiased = pmf.Copy()
    unbiased.name = name

    for x, _ in unbiased.Items():
        unbiased.Mult(x, 1.0/x)

    unbiased.Normalize()
    return unbiased

def BiasPmf(pmf, value, name):
    biased = pmf.Copy()
    biased.name = name

    for x, _ in biased.Items():
        biased.Mult(x, abs(x-value))

    biased.Normalize()
    return biased


def main():
    # Exercise 3.1
    d = {
        7: 8,
        12: 8,
        17: 14,
        22: 4,
        27: 6,
        32: 12,
        37: 8,
        42: 3,
        47: 2
    }

    classSizeDean = Pmf.MakePmfFromDict(d, name='Actual')
    print(classSizeDean.Mean())

    classSizeStudent = classSizeDean.Copy(name='Student Perspective')
    for x, _ in classSizeStudent.Items():
        classSizeStudent.Mult(x, x)
    classSizeStudent.Normalize()
    print(classSizeStudent.Mean())

    classSizeUnbaised = UnbiasPmf(classSizeStudent, 'Student Unbiased')
    print(classSizeUnbaised.Mean())

    getValue = itemgetter(0)

    deanPlot = sorted(classSizeDean.Items(), key=getValue)
    studentPlot = sorted(classSizeStudent.Items(), key=getValue)
    plt.plot(zip(*deanPlot)[0], zip(*deanPlot)[1], 'g-', label='Actual')
    plt.plot(zip(*studentPlot)[0], zip(*studentPlot)[1], 'r-', label='Student Perspective')
    plt.legend(loc=4)
    plt.xlabel('Class Size')
    plt.ylabel('Probability')
    plt.show()

    #Exercise 3.2
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    unbaisedSpeedsPmf = Pmf.MakePmfFromList(speeds, 'speeds')
    biasedSpeedsPmf = BiasPmf(unbaisedSpeedsPmf, 7.5, '7.5 mph biased speeds')

    biasedPlot = sorted(biasedSpeedsPmf.Items(), key=getValue)
    myplot.Pmf(biasedSpeedsPmf)
    myplot.Show(title='7.5mph biased speeds',
                xlabel='speeds (mph)',
                ylabel='probability')

if __name__ == "__main__":
    main()
