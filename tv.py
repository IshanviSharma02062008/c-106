import csv
import numpy as np


def getDataSource(data_path):
    Average_time_spent_watching_TV_in_a_week = []
    Size_of_tv = []
    with open("tv.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Average_time_spent_watching_TV_in_a_week .append(float(row["Average time spent watching TV in a week "]))
            Size_of_tv.append(float(row["Size of tv"]))

    return {"x" :Average_time_spent_watching_TV_in_a_week , "y": Size_of_tv}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Average time spent watching TV in a week and Size of tv :-  \n--->",correlation[0,1])

def setup():
    data_path  = "tv.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()