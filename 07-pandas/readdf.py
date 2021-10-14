# Import libraries
import numpy as np
import pandas as pd


def process(path):
    """
    Given the path to a CSV file as input, selects those
    entries with a valid license (not NaN), room type of Private room, price less than or equal to 80, minimum nights
    less than or equal to 2, number of reviewers more than or equal to 500, or those with a valid license (not NaN),
    a room type of Entire home/apt, price less than or equal to 100, minimum nights less than or equal to 1,
    number of reviewers more than or equal to 100, and finally present the result sorted according to latitude and
    then longitude in an ascending order and with only columns of id, latitude, longitude, room_type,
    price and availability_365.
    :param path: path to csv file to load in.
    :return: processed pandas dataframe
    """
    # Read in dataframe (original size: (16478, 18)):
    df1 = pd.read_csv(path)
    # Drop License NA (new dim: (4135, 18)):
    df1.dropna(how="any", subset=["license"], inplace=True)
    # Filter dataframe:
    df2 = df1[((df1["room_type"] == "Private room") & (df1["price"] <= 80) & (df1["minimum_nights"]) <= 2 & (df1['number_of_reviews'] >= 500))]
    df3 = df1[((df1["room_type"] == "Entire home/apt") & (df1["price"] <= 100) & (df1["minimum_nights"] <= 1) & (df1['number_of_reviews'] >= 100))]
    # Merge the two dataframes:
    df4 = pd.concat([df2, df3], axis=0)
    # df1 = df1[(((df1["room_type"] == "Private room") & (df1["price"] <= 80) & (df1["minimum_nights"]) <= 2 & (df1['number_of_reviews'] >= 500)) or
    #            ((df1["room_type"] == "Entire home/apt") & (df1["price"] <= 100) & (df1["minimum_nights"] <= 1) & (df1['number_of_reviews'] >= 100)))]
    # Subset columns:
    df4 = df4[["id", "latitude", "longitude", "room_type", "price", "availability_365"]]
    # Sort on latitude and longitude:
    df4 = df4.sort_values(by=["latitude", "longitude"], ascending=True)
    return df4


df = process('listings.csv')
print(f"Dimensions: {df.shape}")
print(f"Column names:")
print(df.columns)
print(df)


