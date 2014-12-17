import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)


loansData.boxplot(column=['Amount.Funded.By.Investors','Amount.Requested'])
plt.title("Boxplot")
plt.show()

loansData.hist(column=['Amount.Funded.By.Investors','Amount.Requested'])
plt.title("Histogram")
plt.show()



plt.figure()

graph1 = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)

graph2 = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)

plt.title("Distribution of Loan Amounts")
plt.show()
# are they suppose to be very similar