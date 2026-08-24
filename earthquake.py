# final earthquake class

"""

Module: earthquake.py

Project: Earthquake Disaster Monitoring and Seismic Risk Analysis System

Description:
This module defines the Earthquake class, which represents a single earthquake
event obtained from the United States Geological Survey (USGS) Earthquake
Catalog.

Each Earthquake object stores important seismic information including
magnitude, location, geographic coordinates, depth, and occurrence time.
The class also provides methods to classify earthquake severity,
display earthquake information, and compare earthquake objects.

"""

from datetime import datetime


class Earthquake:
    """
    Represents a single earthquake event.

    Description:
        The Earthquake class stores the physical and geographic properties
        of one earthquake. It also provides methods for classifying the
        earthquake's severity, displaying its information, and comparing
        one earthquake object with another.

    Attributes:
        magnitude (float):
            Magnitude of the earthquake.

        location (str):
            Name or description of the earthquake location.

        latitude (float):
            Latitude coordinate of the earthquake.

        longitude (float):
            Longitude coordinate of the earthquake.

        depth (float):
            Depth of the earthquake in kilometers.

        event_time (datetime):
            Date and time when the earthquake occurred.
    """

    def __init__(
        self,
        magnitude,
        location,
        latitude,
        longitude,
        depth,
        event_time
    ):
        """
        Initializes an Earthquake object.

        Description:
            Creates a new Earthquake object using the provided earthquake
            information. The constructor validates the magnitude and depth
            values before storing them as object attributes.

        Parameters:
            magnitude (float):
                Earthquake magnitude.

            location (str):
                Earthquake location.

            latitude (float):
                Latitude coordinate.

            longitude (float):
                Longitude coordinate.

            depth (float):
                Earthquake depth in kilometers.

            event_time (str or datetime):
                Date and time of the earthquake.
                If a string is provided, it must follow ISO format.

        Returns:
            None

        Raises:
            ValueError:
                If magnitude or depth is negative.
        """

        # Earthquake magnitude cannot be negative.
        if magnitude < 0:
            raise ValueError("Magnitude cannot be negative.")

        # Earthquake depth cannot be negative.
        if depth < 0:
            raise ValueError("Depth cannot be negative.")

        # Store earthquake information as object attributes.
        self.magnitude = float(magnitude)
        self.location = location
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.depth = float(depth)

        # Convert the input string into a datetime object if necessary.
        if isinstance(event_time, str):
            self.event_time = datetime.fromisoformat(event_time)
        else:
            self.event_time = event_time

    def severity_category(self):
        """
        Determines the earthquake severity category.

        Description:
            Classifies the earthquake according to its magnitude using
            standard USGS earthquake magnitude classifications.

        Parameters:
            None

        Returns:
            str:
                The earthquake severity category.

                Possible values include:
                - Micro
                - Minor
                - Light
                - Moderate
                - Strong
                - Major
                - Great
        """

        # Determine the severity based on earthquake magnitude.
        if self.magnitude < 2.0:
            return "Micro"

        elif self.magnitude < 4.0:
            return "Minor"

        elif self.magnitude < 5.0:
            return "Light"

        elif self.magnitude < 6.0:
            return "Moderate"

        elif self.magnitude < 7.0:
            return "Strong"

        elif self.magnitude < 8.0:
            return "Major"

        else:
            return "Great"

    def __str__(self):
        """
        Returns a readable string representation of the earthquake.

        Description:
            Formats the earthquake information into a human readable string
            that can be displayed or printed.

        Parameters:
            None

        Returns:
            str:
                A formatted description of the earthquake.
        """

        return (
            f"Earthquake\n"
            f"-----------\n"
            f"Magnitude : {self.magnitude}\n"
            f"Category  : {self.severity_category()}\n"
            f"Location  : {self.location}\n"
            f"Latitude  : {self.latitude}\n"
            f"Longitude : {self.longitude}\n"
            f"Depth     : {self.depth} km\n"
            f"Date/Time : {self.event_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def __eq__(self, other):
        """
        Compares two Earthquake objects.

        Description:
            Determines whether two earthquake objects represent the same
            earthquake event by comparing their magnitude, location,
            and occurrence time.

        Parameters:
            other (Earthquake):
                Another Earthquake object.

        Returns:
            bool:
                True if both objects represent the same earthquake;
                otherwise False.
        """

        # Ensure the object being compared is an Earthquake object.
        if not isinstance(other, Earthquake):
            return False

        # Compare important earthquake attributes.
        return (
            self.magnitude == other.magnitude
            and self.location == other.location
            and self.event_time == other.event_time
        )


# This block only executes when earthquake.py is run directly.
# It does not execute when the module is imported into another file.
if __name__ == "__main__":

    earthquake = Earthquake(
        magnitude=6.5,
        location="California",
        latitude=36.7783,
        longitude=-119.4179,
        depth=12.5,
        event_time="2025-01-15T08:30:00"
    )

    print(earthquake)