#The data Entries in columns 'cases','deaths','tests' had dictonaries in their data so we need to normalize the data
import pandas as pd

df = pd.read_csv('datasets/covid-193.csv')

#Normalize columns in df-'cases','deaths','tests'
cases_df = pd.json_normalize(df['cases'].apply(eval))
deaths_df = pd.json_normalize(df['deaths'].apply(eval))
tests_df = pd.json_normalize(df['tests'].apply(eval))


#create prefixes to avoid confusion
cases_df.columns = ['cases_' + col for col in cases_df.columns]
deaths_df.columns = ['deaths_' + col for col in deaths_df.columns]
tests_df.columns = ['tests' + col for col in tests_df.columns]

df = pd.concat([df, cases_df, deaths_df,tests_df], axis=1)

df = df.drop(columns=['cases', 'deaths','tests'])
