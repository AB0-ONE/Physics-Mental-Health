import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/sandra/Desktop/DAV_TKU_Project/Data/mental_health_physical_activity.csv"
)
print(df.columns)
print(df.info()) 

df = df[[
    "Anxiety_Level",
    "Stress_Level",
    "Depression_Level",
    "Happiness_Level",
    "Mental_Health_Score"
]].dropna()

print(df.isna().sum())
print(df.head())
print(df.describe())

corr = df.corr()


plt.figure(figsize=(12, 10))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("/Users/sandra/desktop/DAV_TKU_Project/Plots/Heatmap.png")
plt.show()

