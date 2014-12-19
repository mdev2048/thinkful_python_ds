import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
# print loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
# 81174     8.90%
# 99592    12.12%
# 80059    21.98%
# 15825     9.99%
# 33182    11.71%
# Name: Interest.Rate, dtype: object

# print loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
# 81174    36 months
# 99592    36 months
# 80059    60 months
# 15825    36 months
# 33182    36 months
# Name: Loan.Length, dtype: object

# print loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range
# 81174    735-739
# 99592    715-719
# 80059    690-694
# 15825    695-699
# 33182    695-699
# Name: FICO.Range, dtype: object

#example of lambda funct vs regular func
def f(x):
    '''This function takes x as a parameter and returns x squared'''
    print x**2

g = lambda x: x**2

# Remove the '%' symbols from the Interest.Rate column.
loansData["Interest.Rate"] =  map(lambda s: s.replace("%",""), loansData["Interest.Rate"])
# print loansData["Interest.Rate"][:5]

# Remove the word 'months' from the Loan.Length column.
loansData['Loan.Length'] = map(lambda s: s.replace(" months",""),loansData['Loan.Length'])
# print loansData['Loan.Length'][:5]



# Convert FICO scores into a numerical value, and save it in a new column called FICO.Score. 
# Since the ranges are small, we're going to go ahead and pick the first number to represent 
# the range.
tempFicoRange = loansData['FICO.Range'].tolist()
tgtFICO = []
# apparently, fico score is just the average of the Fico-range
for idx in range(len(tempFicoRange)):
	curFicoScore = np.mean([int(x) for x in tempFicoRange[idx].split("-")])
	tgtFICO.append(curFicoScore)

loansData["FICO.Score"] = tgtFICO

p = loansData["FICO.Score"].hist()
plt.title("FICO Score Historgram")
plt.show()



# ISSUE: scatter matrix does not display Interest Rate 
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.title("Loans Data Scatter Matrix")
plt.show()

# p = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()


# Where do you see a noticeable trend in the scatterplot? 

# Where don't you see a noticeable trend? 

# What does this mean in practice?