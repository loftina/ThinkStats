import Pmf
import survey

# Exercise 2.4
# takes a Pmf of lifetimes and an age, and returns a new Pmf that represents the distribution of remaining lifetimes.
def RemainingLifetime(pmf, value):
    remainingPmf = pmf.Copy()
    remainingPmf.Remove(value)
    remainingPmf.Normalize()
    return remainingPmf

# Exercise 2.5
# Write functions called and that take a Pmf object and compute the mean and variance.
# To test these methods, check that they are consistent with the methods and in.

def PmfMean(pmf):
    return sum([var*prob for var, prob in pmf.Items()])

def PmfVar(pmf):
    mean = PmfMean(pmf)
    return sum([prob * (var-mean)**2 for var, prob in pmf.Items()])

table = survey.Pregnancies()
table.ReadRecords()
firstPregLength = [p.prglength for p in table.records if p.birthord == 1 and p.outcome == 1]

print (PmfMean(Pmf.MakePmfFromList(firstPregLength)))
print (PmfVar(Pmf.MakePmfFromList(firstPregLength)))

