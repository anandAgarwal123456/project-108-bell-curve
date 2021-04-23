import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("project-108.csv")
data = df["AvgRating"].tolist()

plot = ff.create_distplot([data], ["Ratings"])
plot.show()

totalRatings=0
totalEntries = 0

for rating in data:
    totalRatings += float(rating)
    totalEntries += 1

mean = totalRatings/totalEntries

print("The mean is: "+ mean)
