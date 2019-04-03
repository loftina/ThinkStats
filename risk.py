import survey
import Pmf

def ProbOnRange(pmf, start, end):
    probability = 0
    for index in range(start, end+1):
        probability += pmf.Prob(index)
    return probability

def ProbEarly(pmf):
    return ProbOnRange(pmf, 0, 37)

def ProbOnTime(pmf):
    return ProbOnRange(pmf, 38, 40)

def ProbLate(pmf):
    return ProbOnRange(pmf, 41, 50)

table = survey.Pregnancies()
table.ReadRecords()
firstPregLengthPmf = Pmf.MakePmfFromList([p.prglength for p in table.records if p.outcome == 1 and p.birthord == 1])
followingPregLengthPmf = Pmf.MakePmfFromList([p.prglength for p in table.records if p.outcome == 1 and p.birthord != 1])
pregLengthPmf = Pmf.MakePmfFromList([p.prglength for p in table.records if p.outcome == 1])

print("First Birth Probabilities:\nEarly: %f\nOn Time: %f\nLate: %f\n" %
      (ProbEarly(firstPregLengthPmf),
       ProbOnTime(firstPregLengthPmf),
       ProbLate(firstPregLengthPmf)))
print("Following Birth Probabilities:\nEarly: %f\nOn Time: %f\nLate: %f\n" %
      (ProbEarly(followingPregLengthPmf),
       ProbOnTime(followingPregLengthPmf),
       ProbLate(followingPregLengthPmf)))
print("Total Birth Probabilities:\nEarly: %f\nOn Time: %f\nLate: %f\n" %
      (ProbEarly(pregLengthPmf),
       ProbOnTime(pregLengthPmf),
       ProbLate(pregLengthPmf)))

print("Relative Risk of First vs Following Children:")
earlyRR = ProbEarly(firstPregLengthPmf) / (ProbEarly(followingPregLengthPmf))
print("Relative Risk of Being Born Early: %f" % earlyRR)
onTimeRR = ProbOnTime(firstPregLengthPmf) / (ProbOnTime(followingPregLengthPmf))
print("Relative Risk of Being Born On Time %f" % onTimeRR)
lateRR = ProbLate(firstPregLengthPmf) / (ProbLate(followingPregLengthPmf))
print("Relative Risk of Being Born Late %f" % lateRR)
