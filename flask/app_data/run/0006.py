import pandas as pd

#READ


df = pd.read_csv('../raw/0006/jamesbond.csv', usecols= ['Movie','Kills_Bond','Kills_Others'])
print (df)
# df = pd.read_csv('../raw/0008/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2014-2019.csv', usecols= ['Jurisdiction of Occurrence','MMWR Year','MMWR Week', 'All Cause'],dtype={'Jurisdiction of Occurrence': str,'MMWR Year': int,'MMWR Week': int,'All Cause': int})



df = df.rename(columns={"Kills_Bond": "Kills by Bond", "Kills_Others": "Kills of Others" })

df.to_csv('../processed/0006.csv')