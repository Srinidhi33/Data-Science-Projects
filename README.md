# A Regression model that predicts the number of cases that can be expected based on the population input

> **Introduction**
> This project aims to develop a predictive model for COVID-19 cases using population data. Given the exponential nature
> of COVID-19 spread, log transformation is applied to population and case counts to stabilize variance and improve model
> performance.

> **Data Extraction**
> The dataset was scraped using **Rapid API**  to fetch data from various websites. Rapid API provides a seamless way to
> access and retrieve data from multiple sources, ensuring that the dataset is comprehensive and up-to-date.

> The data can be fetched from Rapid API using an API key for statistics from 'COVID-19', a publicly available API
> hosted by Rapid API.

> The data is scraped from various sources hence it is first converted to CSV, making it persistent, and then the model
> is trained on that data.

> Run the scraper.py file for Scraping the data using API.

> Run the Jupyter Notebook for Data Visualization and Model
