# test_data_loader.py

"""
File: test_data_loader.py

Description:
This test module contains unit tests for the data_loader.py module,
which is responsible for loading earthquake data from CSV files.

"""

import pytest
from data_loader import load_earthquake_data, iter_earthquake_records
from datetime import datetime, timezone


def write_sample_csv(directory, rows):
    """
    Create a USGS-compliant CSV file with the specified rows in the given directory.
    """

    csv_file_path = directory / "sample_earthquake_data.csv" # Write the header and rows to the CSV file
    header = "mag,latitude,longitude,depth,time,place\n"
    csv_file_path.write_text(header + "\n".join(rows), encoding="utf-8") 
    return csv_file_path 

def test_missing_file_raises_file_not_found(tmp_path):
    """
    Test that loading a non-existent CSV file raises a FileNotFoundError.

    """

    non_existent_file = tmp_path / "non_existent.csv" # Attempt to load a non-existent file and expect a FileNotFoundError

    with pytest.raises(FileNotFoundError): 
        load_earthquake_data(non_existent_file) 

def test_valid_row_creates_earthquake_object(tmp_path):
    """
    Test that a valid CSV row creates an Earthquake object with correct attributes.

    """

    rows = [
        "5.2,34.05,-118.25,10.0,2023-01-01T12:00:00Z,Los Angeles"
    ]
    csv_file_path = write_sample_csv(tmp_path, rows) # Create the CSV file with the sample row

    earthquakes = load_earthquake_data(csv_file_path) # Load the earthquake data from the CSV file

    assert len(earthquakes) == 1 # Verify that one Earthquake object was created
    earthquake = earthquakes[0] # Verify the attributes of the created Earthquake object
    assert earthquake.magnitude == 5.2 
    assert earthquake.latitude == 34.05
    assert earthquake.longitude == -118.25
    assert earthquake.depth == 10.0 

    expected_time = datetime.fromisoformat("2023-01-01T12:00:00+00:00") 
    assert earthquake.event_time == expected_time
    assert earthquake.location == "Los Angeles"


def test_row_with_missing_value_is_skipped(tmp_path):
    """
    Test that a CSV row with a missing value is skipped and does not create an Earthquake object.

    """
 
    rows = [
        "5.2,34.05,-118.25,10.0,2023-01-01T12:00:00Z,Los Angeles",
        "4.8,61.2,-149.9,,2023-02-10T12:15:00Z,Alaska"  # Missing depth
    ]
    csv_file_path = write_sample_csv(tmp_path, rows) # Create the CSV file with the sample rows

    earthquakes = load_earthquake_data(csv_file_path) # 

    assert len(earthquakes) == 1  # Only the first row should be loaded
    assert earthquakes[0].location == "Los Angeles"


def test_generator_yields_earthquake_objects(tmp_path):
    """
    Test that the generator yields Earthquake objects one at a time.

    """

    rows = [ # Create sample rows for the CSV file
        "5.2,34.05,-118.25,10.0,2023-01-01T12:00:00Z,Los Angeles",
        "4.8,61.2,-149.9,35.2,2023-02-10T12:15:00Z,Alaska"
    ]
    csv_file_path = write_sample_csv(tmp_path, rows) # Create the CSV file with the sample rows

    generator = iter_earthquake_records(csv_file_path) # Use the generator to yield Earthquake objects

    earthquakes = list(generator) # Convert the generator output to a list for testing

    assert len(earthquakes) == 2  # Verify that two Earthquake objects were yielded
    assert earthquakes[0].location == "Los Angeles"
    assert earthquakes[1].location == "Alaska"
