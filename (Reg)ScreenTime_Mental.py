import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/clean_data_1.csv")
df = df.dropna()

plt.figure()
sns.regplot(x="Screen_Time_Hours", y="Mental_Health_Score", data=df, scatter_kws={"alpha":0.5})
plt.title("Screen Time vs Mental Health")

plt.savefig("/Users/sandra/desktop/DAV_TKU_Project/Plots/(Reg)Screen_Mental.png")
plt.show()





