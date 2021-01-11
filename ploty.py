import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('dane_troll_detection/hashtag_by_tw_count.csv')

df.index = df['hashtag']

df.columns = ['hashtag', 'tweets_count']
# ax, fig = plt.figure()

df.plot.barh(color='midnightblue')

plt.savefig('figures/hashtag_by_tw_count.png', transparent=True)
plt.show()

