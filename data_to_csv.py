#This snippet makes the data persistent by storing all the data into a csv file
from normalizer import df


df.to_csv('datasets/Covid-19 stats.csv', index=False)

print(df.head())
