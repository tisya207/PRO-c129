import pandas as pd 
import csv

df= pd.read_csv("bright_stars.csv")
print(df.shape)

del df["Luminosity"]

print(df.shape)


df.to_csv('data1.csv') 