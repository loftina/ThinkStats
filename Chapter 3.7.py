from __future__ import division

def main():
    # Exercise 3.8

    m4049Position = 26   # the author placed 26th in M4049 division
    m4049Total = 256    # there are 256 men in the division
    rank = 1 - m4049Position/m4049Total
    percentileRank = rank * 100
    print ('percentile rank for m4049 division: %i%%' % int(percentileRank))

    m5059Total = 171
    m5059Position = int((1 - rank) * m5059Total)   # the author would need to place 17th to keep his percentile rank
    authorTimeSec = (42 * 60) + 44
    m505917thTimeSec = (46 * 60) + 05
    expectedSpeedDecrease = m505917thTimeSec - authorTimeSec
    print('%d:%d sec decrease' % (expectedSpeedDecrease/60, expectedSpeedDecrease%60))

    f2039Total = 448
    f2039Position = int((1 - rank) * f2039Total)   # the author's percentile rank corresponds to 45th in f2039
    # the author's friend must beat 48:29 to have a better percentile rank according to these data


if __name__ == "__main__":
    main()
