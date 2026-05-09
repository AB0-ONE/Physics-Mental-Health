import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/sandra/desktop/DAV_TKU_Project/Data/clean_data_1.csv")
df=df.dropna()
df["Screen Time"] = pd.cut(
    df["Screen_Time_Hours"],
    bins=[0, 2, 4, 6, 8, 10, 12],
    labels=["<2", "2-4", "4-6", "6-8", "8-10", "10+"]
)

grouped = df.groupby("Screen Time", observed=True)["Mental_Health_Score"].mean()

plt.figure(figsize=(8,5))
sns.lineplot(x=grouped.index, y=grouped.values)
plt.title("Screen Time & Mental Health Score")

plt.savefig("/Users/sandra/Desktop/DAV_TKU_Project/Plots/(Line)Screen&Mental.png")
plt.show()
