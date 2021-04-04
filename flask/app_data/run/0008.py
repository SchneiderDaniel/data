import pandas as pd

#READ
df = pd.read_csv('../raw/0008/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2014-2019.csv', usecols= ['Jurisdiction of Occurrence','MMWR Year','MMWR Week', 'All Cause'],dtype={'Jurisdiction of Occurrence': str,'MMWR Year': int,'MMWR Week': int,'All Cause': int})

df_us = df[df['Jurisdiction of Occurrence']=='United States']


df2 = pd.read_csv ('../raw/0008/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2020-2021.csv', usecols= ['Jurisdiction of Occurrence','MMWR Year','MMWR Week','All Cause'])

df2_us = df2[df2['Jurisdiction of Occurrence']=='United States']

df2_us = df2_us[df2_us['MMWR Year']==2020]

df2_us['All Cause']=[x.replace(',', '') for x in df2_us['All Cause']]
df2_us['All Cause'].astype(int)

print(df_us)
print(df_us.info())
print(df2_us)
print(df2_us.info())

df_us = df_us.append(df2_us)


df_us = df_us.drop('Jurisdiction of Occurrence', 1)



df_us = df_us.rename(columns={"MMWR Year": "Year", "MMWR Week": "Week","All Cause": "Cause" })

print(df_us)
#WRITE
df_us.to_csv('../processed/0008.csv')

