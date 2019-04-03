import Pmf
from operator import itemgetter
from collections import Counter


def Mode(hist):  # returns list of most frequent values (Values with highest Frequency)
    maxFreq = max(hist.Freqs())
    mode = [val for val in hist.Values() if hist.Freq(val) == maxFreq]
    return mode

def AllModes(hist):  # return list of value-frequency pairs in descending order of frequency
    getFreq = itemgetter(1)
    modeOrdered = sorted(hist.Items(), key=getFreq, reverse=True)
    return modeOrdered

hist = Pmf.MakeHistFromList([1, 2, 2, 3, 3, 3, 3, 5])
print Mode(hist)
print AllModes(hist)