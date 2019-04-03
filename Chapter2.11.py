import Pmf
import survey
def foo(pmf, x): # removes values in pmf less than x (exclusive)
    returnPmf = pmf.Copy()
    for val in returnPmf.Values():
        if val > x: returnPmf.Remove(val)
    returnPmf.Normalize()
    return returnPmf


table = survey.Pregnancies()
table.ReadRecords()
pregLength = [p.prglength for p in table.records if p.outcome == 1]
pregLengthPmf = Pmf.MakePmfFromList(pregLength)
week39Pmf = foo(pregLengthPmf, 39)
print week39Pmf.Prob(39)
