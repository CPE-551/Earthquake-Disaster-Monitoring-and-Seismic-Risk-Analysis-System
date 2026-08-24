# earthquake analyzer class
"""

Module: analyzer.py

Project:
Earthquake Disaster Monitoring and Seismic Risk Analysis System

Description:
    This module contains the EarthquakeAnalyzer class. The class manages
    multiple Earthquake objects and performs seismic data analysis.

    The EarthquakeAnalyzer class demonstrates composition because it contains
    and processes multiple Earthquake objects. It performs statistical
    calculations, earthquake filtering, frequency analysis, and generates
    seismic risk assessment reports.

"""

import numpy as np
from collections import Counter

from earthquake import Earthquake


class EarthquakeAnalyzer:
    """
    Description:
        The EarthquakeAnalyzer class manages a collection of Earthquake
        objects and performs analysis on earthquake data.

    Function:
        - Store multiple earthquake events.
        - Calculate earthquake statistics.
        - Find the strongest earthquake events.
        - Filter earthquakes based on magnitude.
        - Analyze earthquake severity frequency.
        - Generate seismic risk reports.

    Attributes:
        earthquakes (list):
            A list containing Earthquake objects.

        analysis_results (dict):
            A dictionary storing calculated earthquake analysis results.
    """

    def __init__(self):
        """
        Description:
            Initializes an EarthquakeAnalyzer object.

        Function:
            Creates an empty earthquake collection and an empty dictionary
            for storing analysis results.

        Parameters:
            None

        Returns:
            None
        """

        # Store all Earthquake objects in a list.
        # This demonstrates composition because the analyzer contains
        # multiple Earthquake objects.
        self.earthquakes = []

        # Store calculated results such as averages, frequency counts,
        # and risk information.
        self.analysis_results = {}

    def add_earthquake(self, earthquake):
        """
        Description:
            Adds a single Earthquake object into the analyzer collection.

        Function:
            Validates the object type and stores the earthquake event
            for future analysis.

        Parameters:
            earthquake (Earthquake):
                An Earthquake object to be added.

        Returns:
            None

        Raises:
            TypeError:
                If the provided object is not an Earthquake object.
        """

        # Check that only Earthquake objects are added.
        # This prevents invalid data from entering the analysis system.
        if not isinstance(earthquake, Earthquake):
            raise TypeError(
                "Only Earthquake objects can be added."
            )

        # Add the validated earthquake object to the collection.
        self.earthquakes.append(earthquake)

    def calculate_average_magnitude(self):
        """
        Description:
            Calculates the average magnitude of all earthquake events.

        Function:
            Extracts earthquake magnitudes and uses NumPy to calculate
            the statistical average.

        Parameters:
            None

        Returns:
            float:
                Average earthquake magnitude.

        Raises:
            ValueError:
                If no earthquake objects exist.
        """

        # Prevent calculations when there is no earthquake data.
        if len(self.earthquakes) == 0:
            raise ValueError(
                "Cannot calculate average without earthquake data."
            )

        # Use list comprehension to collect magnitudes from objects.
        magnitudes = [
            earthquake.magnitude
            for earthquake in self.earthquakes
        ]

        # NumPy provides accurate numerical calculations.
        average = np.mean(magnitudes)

        # Save result for later reporting.
        self.analysis_results["Average Magnitude"] = average

        return average

    def find_strongest_earthquake(self):
        """
        Description:
            Finds the earthquake event with the highest magnitude.

        Function:
            Uses the max() function with a lambda expression to compare
            earthquake objects by magnitude.

        Parameters:
            None

        Returns:
            Earthquake:
                The strongest earthquake object.

        Raises:
            ValueError:
                If no earthquake objects exist.
        """

        # Ensure earthquake data exists before searching.
        if len(self.earthquakes) == 0:
            raise ValueError(
                "No earthquake data available."
            )

        # Lambda extracts magnitude from each Earthquake object.
        # max() returns the object with the largest magnitude.
        strongest = max(
            self.earthquakes,
            key=lambda earthquake: earthquake.magnitude
        )

        # Store result.
        self.analysis_results["Strongest Earthquake"] = strongest

        return strongest

    def filter_by_magnitude(self, minimum_magnitude):
        """
        Description:
            Finds earthquakes above a specified magnitude threshold.

        Function:
            Filters earthquake events based on user defined magnitude.

        Parameters:
            minimum_magnitude (float):
                Minimum magnitude value.

        Returns:
            list:
                A list of Earthquake objects matching the condition.

        Raises:
            ValueError:
                If the magnitude threshold is negative.
        """

        # Magnitude cannot be negative.
        if minimum_magnitude < 0:
            raise ValueError(
                "Minimum magnitude cannot be negative."
            )

        # Use list comprehension to filter earthquake events.
        filtered_events = [
            earthquake
            for earthquake in self.earthquakes
            if earthquake.magnitude >= minimum_magnitude
        ]

        return filtered_events

    def analyze_frequency(self):
        """
        Description:
            Counts earthquakes by severity category.

        Function:
            Uses each earthquake object's severity category and counts
            how frequently each category occurs.

        Parameters:
            None

        Returns:
            dict:
                Dictionary containing earthquake category frequencies.
        """

        # Generate a list of severity categories.
        categories = [
            earthquake.severity_category()
            for earthquake in self.earthquakes
        ]

        # Counter counts repeated earthquake categories.
        frequency = dict(
            Counter(categories)
        )

        # Save frequency information.
        self.analysis_results["Frequency"] = frequency

        return frequency

    def generate_risk_report(self):
        """
        Description:
            Creates a seismic risk assessment report.

        Function:
            Combines earthquake statistics into a summary dictionary
            containing total events, average magnitude, strongest event,
            and high risk earthquake count.

        Parameters:
            None

        Returns:
            dict:
                Complete earthquake risk assessment report.

        Raises:
            ValueError:
                If no earthquake data exists.
        """

        # Verify that earthquake data is available.
        if len(self.earthquakes) == 0:
            raise ValueError(
                "Cannot generate report without earthquake data."
            )

        # Calculate required analysis values.
        average = self.calculate_average_magnitude()

        strongest = self.find_strongest_earthquake()

        frequency = self.analyze_frequency()

        # Count earthquakes with magnitude 6.0 or greater.
        # These earthquakes represent higher seismic risk.
        high_risk_count = sum(
            1
            for earthquake in self.earthquakes
            if earthquake.magnitude >= 6.0
        )

        # Create final report dictionary.
        report = {
            "Total Earthquakes": len(self.earthquakes),
            "Average Magnitude": round(
                float(average),
                2
            ),
            "Strongest Magnitude": strongest.magnitude,
            "Strongest Location": strongest.location,
            "High Risk Earthquakes": high_risk_count,
            "Frequency": frequency
        }

        # Store report results.
        self.analysis_results = report

        return report


if __name__ == "__main__":

    """
    Test section:
        Creates sample earthquake objects and verifies that the analyzer
        functions correctly.
    """

    analyzer = EarthquakeAnalyzer()

    earthquake1 = Earthquake(
        magnitude=6.5,
        location="California",
        latitude=36.7783,
        longitude=-119.4179,
        depth=12.5,
        event_time="2025-01-15T08:30:00"
    )

    earthquake2 = Earthquake(
        magnitude=4.8,
        location="Alaska",
        latitude=61.2181,
        longitude=-149.9003,
        depth=35.2,
        event_time="2025-02-10T12:15:00"
    )

    # Add earthquake objects to analyzer.
    analyzer.add_earthquake(earthquake1)
    analyzer.add_earthquake(earthquake2)

    print("\nAverage Magnitude:")
    print(analyzer.calculate_average_magnitude())

    print("\nStrongest Earthquake:")
    print(analyzer.find_strongest_earthquake())

    print("\nFiltered Earthquakes:")
    print(analyzer.filter_by_magnitude(5.0))

    print("\nFrequency Analysis:")
    print(analyzer.analyze_frequency())

    print("\nRisk Report:")
    print(analyzer.generate_risk_report())