# data loader and risk report generation
"""

Module: dataprocessing.py

Project:
Earthquake Disaster Monitoring and Seismic Risk Analysis System

Description:
    This module contains the load_earthquake_data() function, which shall read USGS earthquake
    record datasets, and convert the raw data into usable Python objects. CSV compat data
    shall be read using Pandas and EarthquakAnalyzer shall be used for object comparison.

    This module shall also contain the export_risk_report() function, which shall take the provided
    report and save it into an extractable CSV file.
    
"""

import pandas as pd

from earthquake import Earthquake
from earthquakeanalyzer import EarthquakeAnalyzer

def load_earthquake_data(file_path):
    """
    Description:
        The load_earthquake_data function shall acquire and load data from USGS CSV file.
    
        Function:
            -Returns an analyzer containing all valid earthquake events.
            -Returns FileNotFoundError if the CSV file cannot be found.
            -Returns ValueError if the required columns are missing from the dataset
    
        Attributes:
            file_path(str):
                The location of the CSV file containing the USGS dataset.

    """

    try:
        data = pd.read_csv(file_path) #Extracting and reading the dataset.
    except FileNotFoundError:
        raise FileNotFoundError(
            "The requested earthquake dataset file cannot be found."
        )

    dataset_columns = [ # Columns extracted from the CVS dataset file which shall create the
                        # Earthquake object.
        "mag",
        "latitude",
        "longitude",
        "depth",
        "time",
        "place"
    ]

    for column in dataset_columns:
        if column not in data.columns:
            raise ValueError(
                f"The provided USGS dataset is missing the required column: {column}"
            )

    analyzer = EarthquakeAnalyzer()

    # We will loop through each row of the CSV file to extract the required data and assign it
    # to attributes.
    for magnitude, location, latitude, longitude, depth, event_time in zip(
        data["mag"],
        data["place"],
        data["latitude"],
        data["longitude"],
        data["depth"],
        data["time"]
    ):
        
        try:
            earthquake = Earthquake(
                magnitude = magnitude,
                latitude = latitude,
                longitude = longitude,
                depth = depth,
                event_time = event_time,
                location = location
            )

            # Individual earthqauke object has been created from the dataset attributes.
            # Now we add this to the analyzer.
            analyzer.add_earthquake(earthquake)

        except(ValueError, TypeError) as error:
            raise ValueError(
                f"Invalid earthquake data: {error}"
            )
    return analyzer

    # Now we export the data into an individual separate CSV value.

def export_risk_report(report, output_file):
    """
    Description:
        The export_risk_report function shall acquire and load the analyzed data into a separate
        CSV report.
        
        Function:
            -A dictionary shall be created containing the earthquake analysis results.
            -The created CSV file, earthquake_risk_report, shall provide the path.
    """

    with open(output_file, "w") as f:
        f.write("Category, Value\n") # Creating the column headings.

        # Summarizing the results in the CSV report:
        f.write(
            f"Total Earthquakes Analyzed, {report['Total Earthquakes']}\n"
        )

        f.write(
            f"Average Magnitude of all Events, {report['Average Magnitude']}\n"
        )

        f.write(
            f"Strongest Magnitude of all Events, {report['Strongest Magnitude']}\n"
        )

        f.write(
            f"Strongest Location, {report['Strongest Location']}\n"
        )

        f.write(
            f"High Risk Earthquakes, {report['High Risk Earthquakes']}\n"
        )

        for category, count in report["Frequency"].items():
            f.write(
                f"{category} Earthquakes, {count}\n"
            )

if __name__ == "__main__":
    # Ensure that the earthquake data is saved into a "data" folder within the path.
    analyzer = load_earthquake_data("data/query.csv")

    earthquake_report = analyzer.generate_risk_report()

    # Earthquake risk report shall be generated in an outputs folder within the path.
    export_risk_report(earthquake_report, "outputs/earthquake_risk_report.csv")

    print("Earthquake data loaded successfully.")
    print("Risk report has been created successfully.")
