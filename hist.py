import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df = pd.read_csv('./forsen_viewer_info_2018.07.24_20.04.34.csv')
# df = pd.read_csv('./lirik_viewer_info_2018.07.24_20.02.54.csv')
df = pd.read_csv('./asmongold_viewer_info_2018.07.25_23.44.59.csv')
df = pd.to_datetime(df['created_at'], errors='ignore')
# df = pd.DataFrame(np.random.choice(pd.date_range(start=pd.to_datetime('2015-01-14'),periods = 10000, freq='S'), 500),  columns=['date'])
# df.apply(lambda d: )
print(df)
df = pd.DataFrame(df)
df.set_index('created_at', drop=False, inplace=True)

# hist = df.groupby(pd.Grouper(freq='1M')).count().plot(kind='bar')


# df = df[(df['created_at'] < '2018-03-10') & (df['created_at'] < '2018-03-2')]
hist = df.groupby(pd.Grouper(freq='1M')).count().plot(kind='bar')
xtl=[item.get_text()[0:10] for item in hist.get_xticklabels()]
_=hist.set_xticklabels(xtl)

# hist.plot()
plt.show()
# # print(
# # df[0:10]
# # )

