# visualization.py
"""

Module: visualization.py

Course: CPE 551 - Engineering Programming: Python

Project:
Earthquake Disaster Monitoring and Seismic Risk Analysis System

Description:
    This module provides visualization functions for earthquake analysis.

    Matplotlib is used to create graphical representations of earthquake
    activity, including magnitude distributions, earthquake frequency trends,
    and relationships between earthquake depth and magnitude.

Functions:
    plot_magnitude_distribution():
        Creates a histogram showing earthquake magnitude distribution.

    plot_frequency_distribution():
        Creates a bar chart showing earthquake severity frequency.

    plot_depth_vs_magnitude():
        Creates a scatter plot showing the relationship between earthquake
        depth and magnitude.


"""


import matplotlib.pyplot as plt


def plot_magnitude_distribution(earthquakes):
    """
    Description:
        Creates a histogram displaying earthquake magnitude distribution.

    Function:
        Extracts earthquake magnitudes and displays how frequently different
        magnitude ranges occur.

    Parameters:
        earthquakes (list):
            List containing Earthquake objects.

    Returns:
        None

    """

    # Extract magnitude values from Earthquake objects.
    # List comprehension creates a new list containing only magnitudes.
    magnitudes = [
        earthquake.magnitude
        for earthquake in earthquakes
    ]


    # Create histogram visualization.
    # Histograms help identify earthquake magnitude patterns.
    plt.figure(figsize=(8, 5))

    plt.hist(
        magnitudes,
        bins=10,
        color="orange",
        edgecolor="black"
    )


    # Add chart labels.
    plt.title(
        "Earthquake Magnitude Distribution"
    )

    plt.xlabel(
        "Magnitude"
    )

    plt.ylabel(
        "Number of Earthquakes"
    )


    # Display the chart.
    plt.grid(True)

    plt.show()



def plot_frequency_distribution(frequency_data):
    """
    Description:
        Creates a bar chart showing earthquake frequency by severity.

    Function:
        Displays how many earthquakes occurred in each severity category.

    Parameters:
        frequency_data (dict):
            Dictionary containing earthquake categories and counts.

    Returns:
        None
    """


    # Extract categories and frequency values from dictionary.
    categories = list(
        frequency_data.keys()
    )

    counts = list(
        frequency_data.values()
    )


    # Create bar chart.
    plt.figure(figsize=(8, 5))


    plt.bar(
        categories,
        counts,
        color="blue"
    )


    # Add chart information.
    plt.title(
        "Earthquake Frequency by Severity Category"
    )

    plt.xlabel(
        "Severity Category"
    )

    plt.ylabel(
        "Number of Earthquakes"
    )


    # Rotate labels for better readability.
    plt.xticks(
        rotation=45
    )


    plt.grid(
        axis="y"
    )


    plt.show()



def plot_depth_vs_magnitude(earthquakes):
    """
    Description:
        Creates a scatter plot showing the relationship between earthquake
        depth and magnitude.

    Function:
        Compares earthquake depth with magnitude to identify possible
        relationships between depth and earthquake strength.

    Parameters:
        earthquakes (list):
            List containing Earthquake objects.

    Returns:
        None
    """


    # Extract depth values from earthquake objects.
    depths = [
        earthquake.depth
        for earthquake in earthquakes
    ]


    # Extract magnitude values from earthquake objects.
    magnitudes = [
        earthquake.magnitude
        for earthquake in earthquakes
    ]


    # Create scatter plot.
    # Scatter plots are useful for identifying relationships between variables.
    plt.figure(figsize=(8, 5))


    plt.scatter(
        depths,
        magnitudes,
        color="red",
        alpha=0.6
    )


    # Add chart labels.
    plt.title(
        "Relationship Between Earthquake Depth and Magnitude"
    )

    plt.xlabel(
        "Depth (km)"
    )

    plt.ylabel(
        "Magnitude"
    )


    plt.grid(True)

    plt.show()



if __name__ == "__main__":

    """
    Test section:
        Creates sample data and verifies visualization functions.
    """

    from earthquake import Earthquake


    # Create sample earthquake objects.
    sample_earthquakes = [

        Earthquake(
            6.5,
            "California",
            36.7,
            -119.4,
            12.5,
            "2025-01-15T08:30:00"
        ),

        Earthquake(
            4.8,
            "Alaska",
            61.2,
            -149.9,
            35.2,
            "2025-02-10T12:15:00"
        )

    ]


    # Generate example charts.
    plot_magnitude_distribution(
        sample_earthquakes
    )


    plot_depth_vs_magnitude(
        sample_earthquakes
    )