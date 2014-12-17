from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

def chiSquare(observedCnt, expectedCnt):
	return (observedCnt - expectedCnt) * (observedCnt - expectedCnt) / expectedCnt

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print "# of distinct number of credit lines", len(freq.keys())
print "total credit lines", sum(freq.values())
expectedCnt =  sum(freq.values()) / float(len(freq.keys()))
print "expected count for each number of credit lines", expectedCnt

for i in range(0,len(freq.keys())):
	print freq.keys()[i], " : ", chiSquare(freq.values()[i],expectedCnt)
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.ylabel("Count")
plt.xlabel("Open Credit Lines")
plt.show()

chi, p = stats.chisquare(freq.values())


print "Chi-Square distribution",chi,p