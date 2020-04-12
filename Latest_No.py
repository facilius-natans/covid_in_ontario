import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Ontario_Totals_by_Categories.csv')
_= sns.swarmplot(x='Category', y='Numbers', hue='Date', data=df)
plt.title('Ontario Total Numbers of COVID-19 cases in April 2020')
plt.show()
