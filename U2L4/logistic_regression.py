import pandas as pd
import numpy as np 
import statsmodels.api as sm


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
print "Works"
print df[df['Interest.Rate'] == 10].head() # should all be True
print "Doesn't work"
print df[df['Interest.Rate'] == 13].head() # should all be False


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