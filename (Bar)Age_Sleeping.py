import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/sandra/desktop/DAV_TKU_Project/Data/clean_data_1.csv")
df=df.dropna()

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 50, 100],
    labels=["<25", "25-35", "35-50", "50+"]
)

grouped = df.groupby("Age_Group", observed=True)["Sleep_Hours"].mean()

plt.figure(figsize=(8,5))
bars = plt.bar(grouped.index, grouped.values)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,   
        bar.get_height(),                 
        f"{bar.get_height():.2f}",        
        ha='center',
        va='bottom'
    )

plt.gca().set_axisbelow(True)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.xlabel("Age Group")
plt.ylabel("Average Sleeping Hours")
plt.title("Sleeping across Age Groups")

plt.savefig("/Users/sandra/Desktop/DAV_TKU_Project/Plots/(Age)Sleep Distribution.png")
plt.show()
