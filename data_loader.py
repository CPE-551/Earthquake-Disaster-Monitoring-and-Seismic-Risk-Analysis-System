"""
Module: data_loader.py

Project:
Earthquake Disaster Monitoring and Seismic Risk Analysis System

Description:
This module loads earthquake records from a USGS Earthquake Catalog
CSV dataset. It validates the required columns and important data
fields, converts valid records into Earthquake objects, and returns
them as a list.

Functions:
load_earthquake_data():
Reads earthquake records from a CSV file and converts valid
records into Earthquake objects.
"""

import os
import pandas as pd

from earthquake import Earthquake


def load_earthquake_data(file_path):
    """
    Description:
        Loads earthquake records from the USGS Earthquake Catalog dataset.

    Function:
        - Checks whether the dataset file exists.
        - Reads earthquake records using Pandas.
        - Cleans missing or invalid data.
        - Converts each dataset row into an Earthquake object.
        - Returns a list of Earthquake objects.

    Parameters:
        file_path (str):
            Location of the earthquake CSV dataset.

    Returns:
        list:
            A list containing Earthquake objects created from the dataset.

    Raises:
        FileNotFoundError:
            If the dataset file does not exist.

        ValueError:
            If required earthquake data fields are missing or invalid.

        Exception:
            If an unexpected error occurs while loading the dataset.
    """

    # Check whether the dataset file exists.
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    # Read the CSV file using Pandas.
    try:
        earthquake_data = pd.read_csv(file_path)

    except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        raise ValueError(
            f"Unable to read earthquake dataset: {error}"
        ) from error

    except OSError as error:
        raise OSError(
            f"Unable to access earthquake dataset: {error}"
        ) from error

    # Verify that all required USGS columns are available.
    required_columns = [
        "mag",
        "latitude",
        "longitude",
        "depth",
        "time",
        "place"
    ]

    for column in required_columns:
        if column not in earthquake_data.columns:
            raise ValueError(
                f"The dataset is missing the required column: {column}"
            )

    # Store the converted Earthquake objects.
    earthquake_objects = []

    # Process each earthquake record.
    try:
        for _, row in earthquake_data.iterrows():

            # Skip records containing missing required values.
            if (
                pd.isna(row["mag"])
                or pd.isna(row["latitude"])
                or pd.isna(row["longitude"])
                or pd.isna(row["depth"])
                or pd.isna(row["time"])
                or pd.isna(row["place"])
            ):
                continue

            # Convert the row into an Earthquake object.
            earthquake = Earthquake(
                magnitude=row["mag"],
                location=row["place"],
                latitude=row["latitude"],
                longitude=row["longitude"],
                depth=row["depth"],
                event_time=row["time"]
            )

            # Add the valid object to the collection.
            earthquake_objects.append(earthquake)

    except (ValueError, TypeError) as error:
        raise ValueError(
            f"Invalid earthquake data: {error}"
        ) from error

    # Return all converted Earthquake objects.
    return earthquake_objects


if __name__ == "__main__":
    """
    Test section:
        Loads the earthquake dataset and displays the number of
        valid records and the first earthquake object.
    """

    try:
        earthquakes = load_earthquake_data(
            "data/earthquakes.csv"
        )

        print(
            f"Loaded {len(earthquakes)} earthquake records."
        )

        # Display the first record if the dataset is not empty.
        if earthquakes:
            print(earthquakes[0])

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Data loading error: {error}")