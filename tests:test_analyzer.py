#tests/test_earthquake.py
"""

File: test_analyzer.py

Description:
    Contains pytest test cases for EarthquakeAnalyzer.

Tests:
    1. Verify average magnitude calculation.
    2. Verify strongest earthquake detection.

"""


from earthquake import Earthquake

from analyzer import EarthquakeAnalyzer



def create_sample_analyzer():
    """
    Description:
        Creates sample earthquake data for testing.

    Returns:
        EarthquakeAnalyzer:
            Analyzer containing sample earthquake objects.
    """


    analyzer = EarthquakeAnalyzer()


    earthquake1 = Earthquake(
        magnitude=5.5,
        location="California",
        latitude=36.7,
        longitude=-119.4,
        depth=10,
        event_time="2025-01-01T10:00:00"
    )


    earthquake2 = Earthquake(
        magnitude=7.2,
        location="Japan",
        latitude=35.6,
        longitude=139.6,
        depth=25,
        event_time="2025-02-01T12:00:00"
    )


    analyzer.add_earthquake(
        earthquake1
    )

    analyzer.add_earthquake(
        earthquake2
    )


    return analyzer



def test_average_magnitude():

    """
    Description:
        Tests whether average magnitude calculation works correctly.

    Returns:
        None
    """


    analyzer = create_sample_analyzer()


    average = analyzer.calculate_average_magnitude()


    # Expected:
    # (5.5 + 7.2) / 2 = 6.35
    assert round(average, 2) == 6.35



def test_find_strongest_earthquake():

    """
    Description:
        Tests whether strongest earthquake is identified correctly.

    Returns:
        None
    """


    analyzer = create_sample_analyzer()


    strongest = analyzer.find_strongest_earthquake()


    assert strongest.magnitude == 7.2

    assert strongest.location == "Japan"