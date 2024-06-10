# Walmart Sales Forecasting

## Overview

This project aims to predict department-wide sales for Walmart stores using historical sales data and various machine learning models. The dataset includes sales data for 45 Walmart stores located in different regions. The project involves data preprocessing, exploratory data analysis, feature engineering, model training, and evaluation.

## Dataset Description

Source: [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data).

You are provided with historical sales data for 45 Walmart stores located in different regions. Each store contains a number of departments, and you are tasked with predicting the department-wide sales for each store.

In addition, Walmart runs several promotional markdown events throughout the year. These markdowns precede prominent holidays, the four largest of which are the Super Bowl, Labour Day, Thanksgiving, and Christmas. The weeks including these holidays are weighted five times higher in the evaluation than non-holiday weeks. Part of the challenge presented by this competition is modelling the effects of markdowns on these holiday weeks in the absence of complete/ideal historical data.

### `stores.csv`

This file contains anonymised information about the 45 stores, indicating the type and size of store.

### `train.csv`

This is the historical training data, which covers from 2010-02-05 to 2012-11-01. Within this file you will find the following fields:

- **Store** - the store number
- **Dept** - the department number
- **Date** - the week
- **Weekly_Sales** - sales for the given department in the given store
- **IsHoliday** - whether the week is a special holiday week

### `test.csv`

This file is identical to `train.csv`, except we have withheld the weekly sales. You must predict the sales for each triplet of store, department, and date in this file.

### `features.csv`

This file contains additional data related to the store, department, and regional activity for the given dates. It contains the following fields:

- **Store** - the store number
- **Date** - the week
- **Temperature** - average temperature in the region
- **Fuel_Price** - cost of fuel in the region
- **MarkDown1-5** - anonymised data related to promotional markdowns that Walmart is running. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA.
- **CPI** - the consumer price index
- **Unemployment** - the unemployment rate
- **IsHoliday** - whether the week is a special holiday week

For convenience, the four holidays fall within the following weeks in the dataset (not all holidays are in the data):

- **Super Bowl**: 12-Feb-10, 11-Feb-11, 10-Feb-12, 8-Feb-13
- **Labour Day**: 10-Sep-10, 9-Sep-11, 7-Sep-12, 6-Sep-13
- **Thanksgiving**: 26-Nov-10, 25-Nov-11, 23-Nov-12, 29-Nov-13
- **Christmas**: 31-Dec-10, 30-Dec-11, 28-Dec-12, 27-Dec-13

## Description

One challenge of modelling retail data is the need to make decisions based on limited history. If Christmas comes but once a year, so does the chance to see how strategic decisions impacted the bottom line.

## Markdowns

In this recruiting competition, job-seekers are provided with historical sales data for 45 Walmart stores located in different regions. Each store contains many departments, and participants must project the sales for each department in each store. To add to the challenge, selected holiday markdown events are included in the dataset. These markdowns are known to affect sales, but it is challenging to predict which departments are affected and the extent of the impact.

Want to work in a great environment with some of the world's largest data sets? This is a chance to display your modelling mettle to the Walmart hiring teams.

This competition counts towards rankings & achievements. If you wish to be considered for an interview at Walmart, check the box "Allow host to contact me" when you make your first entry.

You must compete as an individual in recruiting competitions. You may only use the provided data to make your predictions.

## Evaluation

This competition is evaluated on the weighted mean absolute error (WMAE):

$$WMAE = \frac{1}{\sum w_i} \sum_{i=1}^{n} w_i \lvert y_i - \hat{y_i} \rvert \$$

where

- $`n`$ is the number of rows
- $`\hat{y_i}`$ is the predicted sales
- $`y_i`$ is the actual sales
- $`w_i`$ are weights, where $w = 5$ if the week is a holiday week, and $1$ otherwise

## Submission File

For each row in the test set (store + department + date triplet), you should predict the weekly sales of that department. The Id column is formed by concatenating the Store, Dept, and Date with underscores (e.g. `Store_Dept_2012-11-02`). The file should have a header and look like the following:

Id,Weekly_Sales

1_1_2012-11-02,0

1_1_2012-11-09,0

1_1_2012-11-16,0

## Repository Structure

walmart_forecasting/
    raw_data/
        features.csv
        stores.csv
        train.csv
        test.csv
    data_splits/
        X_train.csv
        X_test.csv
        y_train.csv
        y_test.csv
    processed_data/
        df_train_final.csv
        df_test_final.csv
    Preprocessing.ipynb

## Getting Started

To get started with the project, clone the repository and follow the steps in the `Preprocessing.ipynb` notebook to understand the data preprocessing workflow and how the data is prepared for model training.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
