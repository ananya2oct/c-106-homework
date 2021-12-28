import csv
import plotly.express as px
import numpy as np


def getDataSource(data_path):
    mark_in_percentage=[]
    days_present=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            mark_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x" : mark_in_percentage, "y" : days_present}


def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between marks in percentage and days present: ", correlation[0,1])

def setUp():
    data_path="Student Marks vs Days Present.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

setUp()
