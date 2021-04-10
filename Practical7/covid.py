# import all needed packages.
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# change directory
os.chdir("C:/Users/86135/Desktop/IBI/Week 7")
# import the file
covid_data = pd.read_csv("full_data.csv")
# show all columns.
print(covid_data.info())
# show every second row between 0 and 10
print(covid_data.iloc[0:11:2, 0:])


# use a Boolean to show "total_cases" for all rows corresponding to Afghanistan
def x(country):
    my_columns = []
    for i in covid_data.iloc[:, 1]:
        if i == country:
            a = True
        else:
            a = False
        my_columns.append(a)
    return my_columns
print(covid_data.loc[x("Afghanistan"), "total_cases"])

# compute the mean and median of new cases for the world
world_new_cases = covid_data.loc[x("World"), "new_cases"]
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print("mean=", mean)
print("median=", median)

# plot a boxplot of new cases worldwide.
plt.boxplot(world_new_cases, whis=1.5, patch_artist=True, meanline=True)
plt.title("New cases worldwide")
plt.show()

# plot both new cases and new deaths worldwide
world_dates = covid_data.loc[x("World"), "date"]
world_new_deaths = covid_data.loc[x("World"), "new_deaths"]
plt.title("New cases and new deaths worldwide")
plt.plot(world_dates, world_new_cases, label="new_cases")
plt.plot(world_dates, world_new_deaths, label="new_deaths")
plt.legend()
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.show()

# another question: How have new cases and total cases developed over time in Spain?
spain_booleans = x("Spain")
spain_new_cases = covid_data.loc[spain_booleans, "new_cases"]
spain_total_cases = covid_data.loc[spain_booleans, "total_cases"]
spain_dates = covid_data.loc[spain_booleans, "date"]
plt.title("New and Total Cases in Spain")
plt.plot(spain_dates, spain_new_cases, "ro", label="New Cases")
plt.plot(spain_dates, spain_total_cases, "bo", label="Total Cases")
plt.legend()
plt.xticks(spain_dates.iloc[0:len(spain_dates):4],rotation=-90)
plt.show()
