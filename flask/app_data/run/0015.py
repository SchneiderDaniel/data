import pandas as pd

#READ


df = pd.read_csv('../raw/0015/index.csv')


def length_of_string(text):

    # if len(text)<11: 
    #     print('_____')
    #     print(text)
    #     print('_____')
    return len(text)

df['Length'] = df.apply(lambda row: length_of_string(row.program) , axis = 1)
df = df.sort_values('Length', ascending=True)

df_result2 = df.groupby(['Length']).size().reset_index(name='counts')


df_result2=df_result2.iloc[5:129]

# print(df_result2.head(100))

df_result2.to_csv('../processed/0016.csv')


list_of_texts = df['program'].tolist()

list_of_unique_text = []
for text in list_of_texts:
    list_of_unique_text+=list(set(text))


result =[[x,list_of_unique_text.count(x)] for x in set(list_of_unique_text)]


df_result = pd.DataFrame.from_records(result)

mapping = {df_result.columns[0]:'character', df_result.columns[1]: 'Frequency'}
df_result = df_result.rename(columns=mapping)
df_result = df_result.sort_values('Frequency', ascending=False)



df_result.drop(df_result[(df_result.character == " ")].index, inplace=True)
df_result.drop(df_result[(df_result.character == "\n")].index, inplace=True)
df_result.drop(df_result[(df_result.character == "\t")].index, inplace=True)
df_result.drop(df_result[(df_result.character == "\r")].index, inplace=True)
df_result.drop(df_result[(df_result.character.str.isalpha())].index, inplace=True)
df_result.drop(df_result[(df_result.character.str.isdigit())].index, inplace=True)


# df_result = df_result.sort_values('1', ascending=True)

df_result = df_result.iloc[:30]

# print(df_result)

# df_result.to_csv('../processed/0015.csv')


# print(df.tail(50))