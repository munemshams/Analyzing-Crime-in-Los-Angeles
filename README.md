# Los Angeles Crime Data Analysis

Los Angeles is known for its sunshine, palm trees, and global entertainment industry. However, with a population approaching **4 million residents**, crime remains an unavoidable challenge for city authorities and communities.

This project analyzes **real crime records from the Los Angeles Police Department (LAPD)** to identify patterns in criminal activity. Using Python-based data analysis and visualization techniques, the project investigates:

- When crimes most frequently occur
- Which areas experience the most night-time crime
- Which victim age groups are most affected

The insights generated can support **data-driven policing strategies, community safety planning, and improved resource allocation**.

---

# Project Overview

This project performs exploratory data analysis (EDA) on LAPD crime records to uncover temporal and demographic patterns in reported incidents.

The analysis focuses on three key questions:

1. Which hour experiences the highest number of crimes?
2. Which LAPD division experiences the most night-time criminal activity?
3. How are crimes distributed across victim age groups?

The project produces both **analytical datasets and visual dashboards** that summarize these findings.

---

# Data Source

The dataset used in this project comes from **Los Angeles City's public crime records**.

The dataset is hosted externally due to size limitations:

https://www.kaggle.com/datasets/munemshariarshams/los-angeles-crime-data

The dataset contains crime incident records including:

- Crime occurrence time
- Police division / geographic area
- Victim demographics
- Offense information

---

# Project Workflow

The analysis follows a structured **data analytics workflow** to ensure reproducible and interpretable results.

## 1. Data Loading

The raw crime dataset is loaded into Python using **pandas**.

Initial inspection ensures:

- Correct column types
- Missing value handling
- Data format consistency

---

## 2. Time-Based Crime Analysis

Crime occurrence times are stored in **24-hour format** under the field `TIME OCC`.

To analyze hourly crime patterns:

- The first two digits of the time field are extracted
- Crimes are grouped by hour
- Hourly crime frequencies are calculated

This analysis identifies the **hour with the highest crime activity**.

---

## 3. Night-Time Crime Analysis

Night-time crimes are defined as incidents occurring between:

- **22:00 – 23:59**
- **00:00 – 03:59**

The dataset is filtered for crimes within this time range.

Crimes are then grouped by **LAPD geographic division (AREA NAME)** to determine which areas experience the highest concentration of night-time activity.

---

## 4. Victim Age Group Analysis

Victim ages are grouped into meaningful categories using `pandas.cut()`.

Age groups include:

- 0–17
- 18–25
- 26–40
- 41–65
- 65+

The number of crimes affecting each group is calculated to understand **which demographic groups are most impacted by crime**.

---

## 5. Data Visualization

The project generates visualizations using **Matplotlib** to clearly communicate results.

Generated visualizations include:

- Crime frequency by hour
- Night-time crimes by LAPD area
- Crime distribution across victim age groups

---

# Key Findings

### Peak Crime Hour

The hour with the highest number of reported crimes is:

**12:00–12:59 (Noon)**

Result stored as:

`peak_crime_hour = 12`

The chart `crime_by_hour.png` visualizes this distribution.

---

### Area With Highest Night-Time Crime

Among the 21 LAPD divisions, **Central Division** reports the highest number of crimes occurring during night hours.

The visualization `night_crime_by_area.png` compares crime frequency across divisions.

---

### Crimes by Victim Age Group

Crimes are distributed across victim age groups and stored in the pandas series:

`victim_ages`

The distribution is visualized in:

`victim_age_groups.png`

---

# Files Included

| File | Description |
|-----|-------------|
| `crimes_analysis.py` | Python script that performs the crime data analysis and generates all outputs |
| `README.md` | Project documentation |
| `outputs/` | Folder containing generated analysis results and visualizations |

---

# Python Libraries Used

The analysis was implemented using the following Python libraries:

| Library | Purpose |
|--------|--------|
| pandas | Data manipulation and analysis |
| numpy | Numerical operations |
| matplotlib | Data visualization |
| seaborn | Enhanced statistical plotting |
| os | File system operations |

---

# Key Outcomes

This project demonstrates the use of Python-based analytics to extract insights from large real-world datasets.

The analysis successfully:

- Identified **peak crime hours**
- Determined **areas with the highest night-time crime rates**
- Analyzed **crime distribution across victim demographics**
- Generated structured datasets and visual dashboards

These findings can support **public safety planning and evidence-based decision making**.

---
