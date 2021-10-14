# Import libraries
import numpy as np
import pandas as pd


def process(path):
    # TODO
    """

    :param path:
    :return:
    Implement a function process() that given the path to a CSV file as input, select those
    entries with a valid license (not NaN), room type of Private room, price less than or equal to 80, minimum nights
    less than or equal to 2, number of reviewers more than or equal to 500, or those with a valid license (not NaN),
    a room type of Entire home/apt, price less than or equal to 100, minimum nights less than or equal to 1,
    number of reviewers more than or equal to 100, and finally present the result sorted according to latitude and
    then longitude in an ascending order and with only columns of id, latitude, longitude, room_type,
    price and availability_365.
    """
    # Read in dataframe (original size: (16478, 18)):
    df1 = pd.read_csv(path)
    # Drop License NA (new dim: (4135, 18)):
    df1.dropna(how="any", subset=["license"], inplace=True)
    # Private room only (1360, 18):
    df1 = df1[df1["room_type"] == "Private room"]
    # Price <= 80 (510, 18)
    df1 = df1[df1["price"] <= 80]
    # Minimum nights <= 1 (196, 18)
    df1 = df1[df1["minimum_nights"] <= 2]
    # Number of reviewers >= 100 (66, 18)
    df1 = df1[df1['number_of_reviews'] >= 100]
    # Subset columns:
    df1 = df1[["id", "latitude", "longitude", "room_type", "price", "availability_365"]]
    # Sort on latitude and longitude:
    df1 = df1.sort_values(by=["latitude", "longitude"], ascending=True)
    return df1


df = process('listings.csv')
print(f"Dimensions: {df.shape}")
print(f"Column names:")
print(df.columns)
print(df)


