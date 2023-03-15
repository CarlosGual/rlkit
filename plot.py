import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/03-10-iql-halfcheetah-medium-v2/03-10-iql-halfcheetah-medium-v2_2023_03_10_15_14_56_0000--s-59894/progress.csv')

plt.plot(df['Epoch'], df['eval/Average Returns'])
plt.grid()
plt.savefig('fig.png')

