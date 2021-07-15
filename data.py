import pandas as pd 
import plotly_express as px 

fileName = input("Enter name of your csv file")
independant = input("Enter name of independant variable")
dependant = input("Enter name of dependant variable")
control = input("Enter name of controlling variable")
title1 = input("Enter title")
type = input("Enter type of graph").lower()

df = pd.read_csv(fileName)

if type == "line" :
    fig=px.line(df,x = independant, y = dependant, color = control, title = title1)
    fig.show()
elif type == "bar":
     fig=px.bar(df,x = independant, y = dependant, color = control, title = title1)
     fig.show()
else :
    print("please choose from line or bar")
