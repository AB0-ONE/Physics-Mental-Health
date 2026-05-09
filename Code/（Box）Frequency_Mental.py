import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/clean_data_1.csv")
df = df.dropna()

plt.figure()
sns.boxplot(x="Exercise_Frequency", y="Mental_Health_Score", data=df)
plt.title("Exercise Frequency vs Mental Health Score")

plt.savefig("/Users/sandra/desktop/DAV_TKU_Project/Plots/Frequency_Mental.png")
plt.show()
