
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(2023)
df = pd.DataFrame(columns=['temp'],data=np.round(np.abs(np.random.normal(size=200,scale=30)),2))
#plt.plot(df.temp)

normales = df[(df.temp > df.temp.median()) & (df.temp <= df.temp.mean())]
anomalias = df[(df.temp <=  df.temp.median()) | (df.temp > df.temp.mean())]

plt.plot(normales.index,normales.temp)
plt.scatter(normales.index,normales.temp)

plt.plot(anomalias.index,anomalias.temp)

plt.show()