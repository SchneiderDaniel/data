import pandas as pd

pd.options.mode.chained_assignment = None

from datetime import datetime


from run_utils import get_randomColors







df = pd.read_csv('../raw/0007/0007.csv')




colors = get_randomColors(len(df.columns)-1)


result_df = pd.DataFrame({'Color':colors})

result_df.to_csv('../processed/0007_2.csv')

print(df)


