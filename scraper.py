#This code scrapes the data from covid-193 portal using Rapid-API key

import requests
import pandas as pd

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"x-rapidapi-key": "caea6e5b6cmsh034a11dca5febdap10775djsn4d16e8e92558",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Assuming data['response'] is a list of countries statistics
    countries_data = data.get('response', [])

    # Convert to DataFrame
    df = pd.DataFrame(countries_data)

    # Display the DataFrame
    print(df.head())
    print(df.shape)# Displaying the first few rows for demonstration
else:
    print(f"Failed to retrieve data: {response.status_code}")
df.to_csv('covid-193.csv')
