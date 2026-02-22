**Los Angeles Crime Data Analysis**

Los Angeles is known for its sunshine, palm trees, and global entertainment industry — but with a population of nearly 4 million people, crime is an unavoidable part of city life.
This project analyzes real LAPD crime data to help identify patterns in:

- When crimes happen

- Where night-time offenses are most common

- Which age groups are most affected

The insights generated here can support better policing strategies, community safety planning, and data-driven resource allocation.

This project uses crimes.csv, a modified version of a dataset sourced from Los Angeles City's Public Record Data.

**Key Questions & Insights**

1️. = Which hour has the highest frequency of crimes?

We extract the first two digits of "TIME OCC" (24-hour military format) and count all offenses by hour.

✔ Result

peak_crime_hour = 12

Noon (12:00–12:59) has the highest volume of reported crimes.

A visualization (crime_by_hour.png) highlights the spike clearly.

2️. Which area has the highest frequency of night crimes?

Night hours are defined as:

22:00–23:59

00:00–03:59

The Central Division experiences the most night-time criminal activity.

The visualization (night_crime_by_area.png) shows how Central compares with all 21 LAPD areas.

3️. How many crimes occur against victims of different age groups?

Using pd.cut, we compute the total crimes affecting each group.

Result is stored in a pandas Series named victim_ages

A bar chart (victim_age_groups.png) visualizes the distribution.

**Files Included**

This repository contains the following files:

Main Files

- crimes_analysis_with_visuals.py	Main script performing analysis + generating plots
  
- crimes.csv	LAPD crime dataset (modified)
  
- README.md	Project documentation
  
Generated Output Files

- hourly_crime_counts.csv	Count of crimes per hour (0–23)

- night_crime_by_area.csv	Night crime frequencies by LAPD area

- victim_age_groups.csv	Crimes by victim age group

- summary.txt	Human-readable summary of all key results

- crime_by_hour.png	Plot of crime count by hour

- night_crime_by_area.png	Plot of night crimes per area

- victim_age_groups.png	Plot of victim age-group distribution
