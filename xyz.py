import pandas as pd

def Unique_Dataframe(dataframe):
    columns = dataframe.columns
    unique = [len(data[column].unique()) for column in columns]
    Output_dataframe = pd.DataFrame(columns)
    Output_dataframe.rename(columns = {0:"columns"},inplace = True)
    Output_dataframe['Unique'] = unique
    Output_dataframe['DataTypes'] = Output_dataframe['columns'].dtypes
    return Output_dataframe

# Pass your DataFrame Here
data = pd.read_csv('train.csv')
result = Unique_Dataframe(data)
print(result)
print(type(result))
