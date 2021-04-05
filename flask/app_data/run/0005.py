import pandas as pd

pd.options.mode.chained_assignment = None

from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')

from run_utils import get_randomColors







df = pd.read_csv('../raw/0005/crypto_tradinds.csv', usecols= ['market_cap','crypto_name','trade_date'], parse_dates=['trade_date'], date_parser=dateparse,dtype={'market_cap': float,'crypto_name': str})



mask = (df['trade_date'].dt.month==9) & (df['trade_date'].dt.day==21)
filtered_df=df.loc[mask]


filtered_df['trade_date'] =pd.DatetimeIndex(filtered_df['trade_date']).year


# filtered_df.drop(['trade_date'], axis=1, inplace=True)



groups = filtered_df.groupby(by='trade_date')

result_dfs = []

for group, dataframe in groups:

    sorted_dataframe=dataframe.sort_values(by=['market_cap'], ascending=False)
    top_dataframe = sorted_dataframe.head(20)

    result_dfs.append(top_dataframe)

    # print(group)
    # print (top_dataframe)


result_df = result_dfs[0]


for i in range(1,len(result_dfs)):
  
    result_df = result_df.append(result_dfs[i], ignore_index=True)


result_df = result_df.rename(columns={"trade_date": "Year", "market_cap": "Market Cap","crypto_name": "Name" })







groups_name = result_df.groupby(by='Name')

colors = get_randomColors(len(groups_name))

print(colors)

mapping = {}

for group,color in zip(groups_name,colors):
    mapping[group[0]]=color

print(mapping)

# result_df['Color']= mapping[result_df['Name']]

result_df['Color'] = result_df.apply(lambda row: mapping.get(row.Name), axis=1)


print(result_df)

result_df.to_csv('../processed/0005.csv')

# df = df[df['trade_date']==2020]

# print(filtered_df)