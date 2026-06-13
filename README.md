# A/B Testing Website Analysis

## Overview

This project analyzes the results of an A/B test conducted on a website landing page to evaluate whether a redesigned (treatment) page improved user conversion rates compared to the original (control) page. Using Python for data analysis and Power BI for interactive visualization, the project combines statistical testing with business intelligence techniques to provide actionable recommendations.

## Business Problem

An organization introduced a redesigned landing page and wanted to determine whether the new design increased user conversions and generated greater business value. This analysis uses A/B testing methodology to compare the performance of the existing and redesigned pages and determine if the observed differences are statistically significant.

## Dataset

The dataset used in this project is publicly available on Kaggle:

**A/B Testing Dataset**  
https://www.kaggle.com/datasets/aadbutt/ab-testing

The dataset contains approximately 270,000 user records and includes information such as user group assignment (control or treatment), conversion status, timestamps, demographic attributes, device type, session metrics, and purchase amounts.

*Note: The dataset was used for educational and portfolio purposes only.*

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels

## Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Hypothesis Testing
- A/B Test Analysis
- Two-Proportion Z-Test
- Data Visualization
- DAX Measure Creation
- Dashboard Design
- Business Intelligence
- Business Recommendations

## Python Analysis

The Python workflow includes:

- Loading and cleaning the dataset
- Checking for duplicates and missing values
- Calculating conversion rates
- Performing a two-proportion Z-test
- Computing relative lift
- Analyzing purchase behavior
- Segmenting conversions by device, location, weekday, and month
- Creating visualizations for business reporting

## Power BI Dashboard

An interactive Power BI dashboard was developed to present the results in a business-friendly format.

Dashboard Features:

- KPI Cards
    - Total Users
    - Overall Conversion Rate
    - Relative Lift
    - Average Purchase Amount
- Conversion Rate by Group
- Monthly Conversion Trend
- Purchase Amount by Group
- Conversion Rate by Device Type
- Conversion Rate by Location
- Interactive Filters and Slicers

## Key Findings

- Treatment conversion rate: 17.95%
- Control conversion rate: 11.87%
- Relative lift: 51.18%
- Statistically significant improvement (p < 0.001)

## Full Results and Dashboard

For results see:
[Business Insights & Recommendations.md](Business_Insights_&_Recommendations.md)

### Dashboard Screenshots:

*Note: See the dashboard pbix file to download or use slicers*

Dashboard Overview:
![Dashboard Overview](visuals/AB_dashboard_1.png)



Control:
![Dashboard Overview 2](visuals/AB_dashboard_2.png)



Treatment:
![Dashboard Overview 3](visuals/AB_dashboard_3.png)