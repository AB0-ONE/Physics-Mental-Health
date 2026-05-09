import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/clean_data_2.csv")
df = df.dropna()

plt.figure()
sns.regplot(x="Exercise_Volume", y="Mental_Health_Score", data=df, scatter_kws={"alpha":0.5})
plt.title("Exercise Volume vs Mental Health")

plt.savefig("/Users/sandra/desktop/DAV_TKU_Project/Plots/(Reg)Exercise_Volume.png")
plt.show()




