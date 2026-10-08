SWYNEX-Final-Data-Analytics-Project
India Air Quality (AQI) Analysis: From Messy Data to Business Insights

Task 4: Final Data Analytics Project | SWYNEX Technologies Internship

This project combines my work from Tasks 1 to 3 into one end-to-end case study: cleaning a messy air quality dataset, exploring it with Python, and presenting the findings in an interactive Power BI dashboard.

Table of Contents:
Problem Statement
Dataset Information
Data Cleaning Process
Exploratory Data Analysis
Interactive Dashboard
Key Business Insights and Recommendations
Tools Used

1. Problem Statement

Air pollution is one of India's most serious public health and environmental challenges. Decision-makers such as city administrations and pollution control bodies need to know which cities have the worst air, how often air quality reaches dangerous levels, and which pollutant matters most. The raw monitoring data, however, is messy: it contains duplicate records, inconsistent city names and date formats, text mixed into numeric fields, invalid sensor readings, and many missing values.

This project cleans the raw AQI data for 10 Indian cities (2023) and analyses it to answer three questions:

Which cities have the highest and lowest air pollution?
How frequently do days fall into unhealthy AQI categories?
Which pollutant is the strongest driver of AQI, so that interventions can be prioritised?

The results are presented in an interactive dashboard so that non-technical stakeholders can explore them by city, AQI category and date.

2. Dataset Information
Item	Details
Raw file	india_aqi_raw_messy.csv (107 rows, 11 columns)
Cleaned file	india_aqi_cleaned.csv (100 rows, 10 columns)
Coverage	10 cities, 1 Jan 2023 to 3 Dec 2023
Cities	Ahmedabad, Bengaluru, Chennai, Delhi, Hyderabad, Jaipur, Kolkata, Lucknow, Mumbai, Pune

Columns (cleaned dataset)

Column	Description	Type
City	City where the reading was recorded	Text
Date	Date of the reading (DD/MM/YYYY)	Date
PM2.5	Fine particulate matter (µg/m³)	Numeric
PM10	Coarse particulate matter (µg/m³)	Numeric
NO2	Nitrogen dioxide	Numeric
SO2	Sulphur dioxide	Numeric
CO	Carbon monoxide	Numeric
O3	Ozone	Numeric
AQI	Air Quality Index value	Numeric
AQI_Bucket	Category: Good, Satisfactory, Moderate, Poor, Very Poor, Severe	Text

Records per city (cleaned): Delhi 22, Chennai 18, Mumbai 15, Jaipur 9, Ahmedabad 8, Lucknow 7, Kolkata 7, Hyderabad 6, Bengaluru 5, Pune 3.

3. Data Cleaning Process

The raw file had problems in almost every column. Each one was found and fixed as follows:

#	Problem found in raw data	How it was fixed
1	7 exact duplicate rows (same reading repeated, only the serial number differed)	Removed duplicates (107 to 100 rows)
2	Inconsistent city names: Delhi, delhi, DELHI, Chennai , MUMBAI (14 variants for 10 cities)	Trimmed spaces and standardised capitalisation
3	Mixed date formats: 03/21/2023, 28/01/2023, 17-01-2023, 2023-01-29	Parsed all formats and converted to a single DD/MM/YYYY format
4	Text in a numeric column: 3 CO values written like 0.28 ppm	Stripped the unit and converted the column to numeric
5	Invalid sensor values: 4 PM10 readings of -999 (a placeholder for "no reading")	Treated as missing values
6	Inconsistent category labels: SEVERE , moderate , very poor, satisfactory (12 spellings for 6 categories)	Trimmed spaces and standardised to Title Case
7	Missing values in every measurement column (about 8 to 10 per column, plus AQI_Bucket)	Numeric columns filled with the column mean; AQI_Bucket filled with the most frequent category
8	Unneeded S.No column	Dropped

Result: a clean dataset with no missing values, no duplicates, correct data types and consistent labels.

4. Exploratory Data Analysis

Script: analysis/exploratory_data_analysis.py (Python, pandas, matplotlib).

Steps: checked shape, columns, missing values and duplicates; calculated summary statistics; computed average AQI per city; counted days per AQI category; measured the correlation of every pollutant with AQI; screened for anomalies using mean ± 2 standard deviations; and created 5 charts.

Headline numbers (cleaned data, n = 100)

Metric	Value
Average AQI	313.8
Maximum AQI	602
Average PM2.5	208.6
Records in the "Severe" category	45

Average AQI by city

Rank	City	Average AQI	Records
1 (worst)	Hyderabad	375.3	6
2	Mumbai	364.7	15
3	Ahmedabad	359.8	8
4	Chennai	336.4	18
5	Lucknow	325.1	7
6	Bengaluru	299.1	5
7	Kolkata	290.6	7
8	Delhi	285.1	22
9	Pune	261.0	3
10 (best)	Jaipur	206.4	9

AQI category distribution: Severe 45, Very Poor 17, Moderate 12, Poor 11, Satisfactory 8, Good 7.

Correlation with AQI

Pollutant	Correlation
PM2.5	0.89
O3	0.14
CO	0.13
PM10	0.07
SO2	0.04
NO2	-0.08

Anomaly check: the normal range (mean ± 2 std) is -24.0 to 651.5. No record falls outside it, so the very high AQI days are part of the regular pattern and not isolated spikes.

Charts

	
Show Image	Show Image
Show Image	Show Image

Show Image

5. Interactive Dashboard

File: dashboard/AQI_Analysis_Dashboard.pbix, built in Microsoft Power BI and titled India Air Quality Analysis: AQI Monitoring Dashboard | 2023.

Show Image

KPI cards

Average AQI
Maximum AQI
Average PM2.5
Severe AQI Records

Charts

AQI Trend Over Time (line chart)
AQI Category Distribution (donut chart)
Average AQI by City (column chart)
Average PM2.5 vs PM10 by City (clustered column chart)

Interactive filters (slicers)

Select City
AQI Category
Date Range

All visuals respond to the slicers, so a viewer can, for example, select one city and see its trend, category mix and pollutant levels in one click.

6. Key Business Insights and Recommendations
#	Insight	Recommendation
1	Poor air quality is the norm, not the exception. The average AQI is 313.8, which sits in the "Very Poor" band, and 62% of records are Very Poor or Severe. Only 15% are Good or Satisfactory.	Treat air quality as a standing public health priority rather than a seasonal problem. Set up year-round health advisories.
2	Hyderabad, Mumbai and Ahmedabad are the most polluted cities in this data (average AQI 360 to 375). Jaipur is the cleanest at 206, a gap of about 169 points.	Focus monitoring and intervention budgets on the top three cities first. Study what keeps Jaipur lower and test whether it can be replicated.
3	PM2.5 is the dominant driver of AQI (correlation 0.89). Every other pollutant is below 0.15.	Prioritise PM2.5 sources: vehicle emissions, construction dust, industrial output and biomass burning.
4	Severe days are part of the normal pattern. No statistical outliers were found even though AQI ranges from 6 to 602. The problem is structural, not caused by rare events.	Plan for continuous, long-term controls and not only emergency measures during "spike" days.
5	AQI changes sharply from day to day (standard deviation of about 169).	Use daily alerts that trigger when AQI crosses the Very Poor and Severe thresholds so people can respond early.
6	Sensor data quality is itself a risk. About 8 to 10% of readings were missing in each column, and some sensors sent invalid -999 values.	Add automated validation and sensor health checks so decisions are based on reliable data.

7. Tools Used
Python (pandas, matplotlib) for cleaning and exploratory analysis
Microsoft Power BI for the interactive dashboard
Git and GitHub for version control and sharing

Completed as Task 4 of the SWYNEX Technologies internship program.
