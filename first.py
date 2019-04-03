from __future__ import division

#1. In the directory where you put survey.py and the data files, create a file named first.py and type or paste in the following code:

import survey

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

#2. Write a loop that iterates table and counts the number of live births. Find the documentation of outcome and confirm that your result is consistent with the summary in the documentation.

liveBirths = 0
for pregnancies in table.records:
    if pregnancies.outcome == 1:
        liveBirths += 1
print 'Number of live births', liveBirths

#3. Modify the loop to partition the live birth records into two groups,one for first babies and one for the others. Again, read the documentation of birthord to see if your results are consistent.
#When you are working with a new dataset, these kinds of checks are useful for finding errors and inconsistencies in the data, detect- ing bugs in your program, and checking your understanding of the way the fields are encoded.

firstLiveBirths = 0
otherLiveBirths = 0
for pregnancies in table.records:
    if pregnancies.outcome == 1:
        if pregnancies.birthord == 1:
            firstLiveBirths += 1
        else:
            otherLiveBirths += 1

print 'Number of live births for first child', firstLiveBirths
print 'Number of live births for following children', otherLiveBirths

#4. Compute the average pregnancy length (in weeks) for first babies and others. Is there a difference between the groups? How big is it?
sumFirstChildWeeks = 0
firstChildCounter = 0
sumFollowingChildWeeks = 0
followingChildCounter = 0
for pregnancies in table.records:
    if pregnancies.outcome == 1:
        if pregnancies.birthord == 1:
            sumFirstChildWeeks += pregnancies.prglength
            firstChildCounter += 1
        else:
            sumFollowingChildWeeks += pregnancies.prglength
            followingChildCounter += 1

avgFirstChild = sumFirstChildWeeks/firstChildCounter
avgFollowingChild = sumFollowingChildWeeks/followingChildCounter
differanceInHours = abs(avgFirstChild - avgFollowingChild) * 7 * 24 #7days 24hours
print 'Average pregnancy length in weeks for live birth first child %.1f' % avgFirstChild
print 'Average pregnancy length in weeks for live birth following children %.1f' % avgFollowingChild
print 'The differance is %.1f hours' % differanceInHours #differance of 13 hours


