import pandas as pd

df=pd.read_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/mental_health_physical_activity.csv")

print(df.columns)
print(df.info()) 

df["Exercise_Volume"]=df["Exercise_Frequency"]*df["Exercise_Duration"]
df = df[[
    'Age',
    'Sleep_Hours',
    'Daily_Steps',
    'Exercise_Frequency',
    'Exercise_Duration',
    'Exercise_Type',
    'Stress_Level',
    'Exercise_Volume'
]].dropna()

#Another: new_data = df.drop(columns=['ID', 
#                                     'Gender',
#                                     ‘Occupation',
#                                     'Exercise_Type',
#                                     'Screen_Time_Hours',      
#                                     'Diet_Quality',
#                                     'Social_Interaction', 
#                                     'Depression_Level',   
#                                     'Happiness_Level',
#                                     'Mental_Health_Score',
#                                     'Notes'])
#        new_data.to_csv("direction/name.csv",index=False)

print(df.isna().sum())
print(df.head())
print(df.describe())

df.to_csv("/Users/sandra/Desktop/DAV_TKU_Project/Data/clean_data.csv",index=False)
