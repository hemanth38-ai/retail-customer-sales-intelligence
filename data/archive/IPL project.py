import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(""C:\Users\hemanth kumar\OneDrive\Desktop\IPL-Data-Analysis\data\matches.csv"")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())