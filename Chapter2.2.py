import thinkstats
import math
import survey


def pumpkin():
    pumpkins = [1, 1, 1, 3, 3, 591]  # pumpkin weights
    mean, variance = thinkstats.MeanVar(pumpkins)
    standardDeviation = math.sqrt(variance)
    return mean, variance, standardDeviation

for p in pumpkin():
    print(p)  # prints mean, variance, and standardDeviation for pumpkin wights


table = survey.Pregnancies()
table.ReadRecords()
firstPregLength = [p.prglength for p in table.records if p.birthord == 1 and p.outcome == 1]
firstPregDeviation = math.sqrt(thinkstats.Var(firstPregLength))
followingPregLength = [p.prglength for p in table.records if p.birthord != 1 and p.outcome == 1]
followingPregDeviation = math.sqrt(thinkstats.Var(followingPregLength))
print (firstPregDeviation, followingPregDeviation)
