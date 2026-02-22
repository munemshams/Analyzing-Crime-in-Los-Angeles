import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------------------
# 1. Load dataset
# --------------------------------------------------------------

df = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})

# Create outputs directory
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# --------------------------------------------------------------
# 2. Extract crime hour
# --------------------------------------------------------------

df["HOUR OCC"] = df["TIME OCC"].str[:2].astype(int)

# --------------------------------------------------------------
# 3. Visualization: Crime frequency by hour
# --------------------------------------------------------------

plt.figure(figsize=(12,5))
sns.countplot(data=df, x="HOUR OCC", color="steelblue")
plt.title("Crime Frequency by Hour of Day")
plt.xlabel("Hour (0–23)")
plt.ylabel("Crime Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "crime_by_hour.png")
plt.show()

# Peak crime hour:
peak_crime_hour = int(df["HOUR OCC"].value_counts().idxmax())
print("Peak crime hour:", peak_crime_hour)

# --------------------------------------------------------------
# 4. Night crime location (22:00–03:59)
# --------------------------------------------------------------

night_hours = [22, 23, 0, 1, 2, 3]
night_df = df[df["HOUR OCC"].isin(night_hours)]

night_counts = (
    night_df.groupby("AREA NAME")["HOUR OCC"]
    .count()
    .sort_values(ascending=False)
)

peak_night_crime_location = night_counts.idxmax()

print("Peak night-crime location:", peak_night_crime_location)

# Visualization
plt.figure(figsize=(12,6))
sns.barplot(x=night_counts.values, y=night_counts.index, palette="mako")
plt.title("Night Crime Frequency by Area (10pm–3:59am)")
plt.xlabel("Crime Count")
plt.ylabel("Area Name")
plt.tight_layout()
plt.savefig(output_dir / "night_crime_by_area.png")
plt.show()

# --------------------------------------------------------------
# 5. Victim age distribution by age groups
# --------------------------------------------------------------

age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

df["Age Bracket"] = pd.cut(
    df["Vict Age"],
    bins=age_bins,
    labels=age_labels
)

victim_ages = df["Age Bracket"].value_counts().reindex(age_labels)
print("\nVictim ages:")
print(victim_ages)

# Visualization
plt.figure(figsize=(10,5))
sns.barplot(x=victim_ages.index, y=victim_ages.values, palette="viridis")
plt.title("Crimes by Victim Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig(output_dir / "victim_age_groups.png")
plt.show()

# --------------------------------------------------------------
# 6. Save output files
# --------------------------------------------------------------

df["HOUR OCC"].value_counts().sort_index().to_csv(output_dir / "hourly_crime_counts.csv")

night_counts.to_csv(output_dir / "night_crime_by_area.csv")

victim_ages.to_csv(output_dir / "victim_age_groups.csv")

# Create a readable summary.txt
with open(output_dir / "summary.txt", "w") as f:
    f.write("Los Angeles Crime Analysis Summary\n")
    f.write("----------------------------------\n\n")
    f.write(f"Peak crime hour: {peak_crime_hour}\n")
    f.write(f"Peak night-crime location: {peak_night_crime_location}\n\n")
    f.write("Victim age distribution:\n")
    for age_group, count in victim_ages.items():
        f.write(f"  {age_group}: {count}\n")

print("\nAll outputs saved in the /outputs folder.")
