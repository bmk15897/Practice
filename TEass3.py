import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("F:/medals.csv",delimiter=',')
recs = len(data)

colors=['r','k','g','y','b','c','m']

for i in range(0,recs):
    plt.bar([i,i+recs+1,i+2*(recs+1)],[data.iat[i,1],data.iat[i,2],data.iat[i,3]],color=colors[i],label=data.iat[i,0],width=1)
plt.ylabel("Medals")
plt.title("Country-wise medal distribution")
plt.legend()
plt.show()