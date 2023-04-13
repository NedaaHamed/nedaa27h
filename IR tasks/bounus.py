import pandas as pd 
bi= pd.read_csv("BI_Software_recommendation_dataset.csv", nrows=5)
print(bi)
newbi = bi.dropna()
print('__________________________________________________________________________________________________________________')
print('\n NUM OF NULL ROWS =',len(newbi))
