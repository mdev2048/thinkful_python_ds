import pandas as pd
import numpy as np 
import statsmodels.api as sm
import math


df = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
df.dropna(inplace=True)

# Add a column to your dataframe indicating whether the interest rate is < 12%.

df["Interest.Rate"] =  map(lambda s: float(s.replace("%","")), df["Interest.Rate"])

# df["IntRateAbv12"] = (df["Interest.Rate"] <= 12.0).astype(int)
df["IntRateAbv12"] = df["Interest.Rate"]
df["IntRateAbv12"] = df['IntRateAbv12'].map(lambda x: x<=12.0)

df['Loan.Length'] = df['Loan.Length'].map(lambda x: x.rstrip('months'))

# FICO SCORE
FICO=[] #declare an empty array
temp = df['FICO.Range'].tolist()
for j in range(len(temp)):   #for j in between 0 to len(A)
  B = temp[j].split("-")     #split each sub-array on - and save it to B
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
df['FICO.Score']=FICO
#print df["IntRateAbv12"]


# Does not work
# print "Works"
# print df[df['Interest.Rate'] == 10].head() # should all be True
# print "Doesn't work"
# print df[df['Interest.Rate'] == 13].head() # should all be False


# Unit 2 Lesson 4 Project 3


intercept = [1] * len(df)
df['Intercept'] = intercept


ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']




# U2L4S3
X = df[ind_vars]
df['IR_TF'] = df['IntRateAbv12']
# Define the logistic regression model. logit = sm.Logit(df['IR_TF'], ind_vars)
logit = sm.Logit(df['IR_TF'], X)
result = logit.fit()
coeff = result.params
print coeff

def getInterestRate(tgtFicoScore, tgtLoanAmount, tgtCoeff):
	b = tgtCoeff['Intercept']
	a1 = tgtCoeff['FICO.Score']
	a2 = tgtCoeff['Amount.Requested']
	curIntRate = a1 * tgtFicoScore + a2 * tgtLoanAmount
	print curIntRate


# Write a function logistic_function that will take a FICO Score and a 
# Loan Amount of this linear predictor, and return p. 
# (Try not to hardcode any values if you can! Hint: pass the 
# coefficients object to the function as an argument.)
def logistic_function(tgtFicoScore, tgtLoanAmount, tgtCoeff):
	b = tgtCoeff['Intercept']
	a1 = tgtCoeff['FICO.Score']
	a2 = tgtCoeff['Amount.Requested']
	demon = (1 + math.exp(b + a1 * tgtFicoScore + a2 * tgtLoanAmount))
	return 1 / demon

print logistic_function(720,10000,coeff)
# Determine the probability that we can obtain a loan at <=12% Interest for $10,000 with a FICO score of 720 using this function.

# Is p above or below 0.70? Do you predict that we will or won't obtain the loan?

# If you're feeling really adventurous, you can create a new function pred to predict whether or not we'll get the loan automatically.

