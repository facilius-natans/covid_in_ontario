import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Ontario_Totals.csv')
_= sns.swarmplot(x='Category', y='Numbers', hue='Date', data=df)
plt.title('Ontario COVID-19 cases in April 2020') 
plt.show() 
