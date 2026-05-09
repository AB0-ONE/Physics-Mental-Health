import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/clean_data_1.csv")

plt.figure()
ax=sns.histplot(df["Mental_Health_Score"], bins=10,kde=True)
for p in ax.patches:
    ax.annotate(
        f"{p.get_height()}",           
        (p.get_x() + p.get_width()/2,      
         p.get_height()),                
        ha='center', va='bottom'
    )
plt.title("Distribution of Mental Health")
plt.savefig("/Users/sandra/Desktop/DAV_TKU_Project/Plots/Mental Health Distribution")
plt.show()
