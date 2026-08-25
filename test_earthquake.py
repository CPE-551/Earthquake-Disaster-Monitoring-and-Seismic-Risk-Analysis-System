# test_earthquake.py

"""
File: test_earthquake.py

Description:
This test module contains pytest test cases for the Earthquake class.

"""
from earthquake import Earthquake
from datetime import datetime
import pytest 



def test_earthquake_creation():

    """
    Test that the Earthquale object is created.
    """
    earthquake = Earthquake(
        magnitude=8.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake.magnitude == 8.1
    assert earthquake.location == "New Jersey"
    assert earthquake.latitude == 40.7440
    assert earthquake.longitude == -74.0324
    assert earthquake.depth == 11.2
    assert earthquake.event_time == datetime(2026, 6, 30, 8, 30, 0)

def test_negative_magnitude_raises_error():

    """
    Test the that an Earthquake object cannot be created if it has a negative magnitude.

    """

    with pytest.raises(ValueError):
        earthquake = Earthquake(
            magnitude=-8.1,
            location="New Jersey",
            latitude=40.7440,
            longitude=-74.0324,
            depth=11.2,
            event_time="2026-06-30T08:30:00"
        )

def test_negative_depth_raises_error():
    """
    Tests the that an Earthquake object cannot be created if it has a negative depth.

    """

    with pytest.raises(ValueError):
        earthquake = Earthquake(
            magnitude=8.1,
            location="New Jersey",
            latitude=40.7440,
            longitude=-74.0324,
            depth=-11.2,
            event_time="2026-06-30T08:30:00"
        )

def test_earthquake_severity():
    """
    Test that the magnitude values are mapping to the correct severity classification.
    """


    earthquake1 = Earthquake(
        magnitude=1.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake1.severity_category() == "Micro"

    earthquake3 = Earthquake(
        magnitude=3.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake3.severity_category() == "Minor"

    earthquake4 = Earthquake(
        magnitude=4.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )
    assert earthquake4.severity_category() == "Light"

    earthquake5 = Earthquake(
        magnitude=5.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake5.severity_category() == "Moderate"


    earthquake6 = Earthquake(
        magnitude=6.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake6.severity_category() == "Strong"


    earthquake7 = Earthquake(
        magnitude=7.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
    )

    assert earthquake7.severity_category() == "Major"

    earthquake8 = Earthquake(
    magnitude=8.1,
    location="New Jersey",
    latitude=40.7440,
    longitude=-74.0324,
    depth=11.2,
    event_time="2026-06-30T08:30:00"
    )

    assert earthquake8.severity_category() == "Great"


def test_eq_same_earthquake():
    """
    Test that whether earthquake objects are "equal" - same location, same magnitude, same event_time
    """

    earthquake_a = Earthquake(
        magnitude=8.1,
        location="New Jersey",
        latitude=50.1240,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
        )

    earthquake_b = Earthquake(
        magnitude=8.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-23.0289,
        depth=15.1,
        event_time="2026-06-30T08:30:00"
        )

    assert earthquake_a == earthquake_b

def test_eq_different_earthquake():
    """
    Test that whether earthquake objects are NOT "equal" - either location, magnitude, or event_time are different
    """

    earthquake_c = Earthquake(
        magnitude=2.1,
        location="New Jersey",
        latitude=50.1240,
        longitude=-74.0324,
        depth=11.2,
        event_time="2026-06-30T08:30:00"
        )

    earthquake_d = Earthquake(
        magnitude=8.1,
        location="New Jersey",
        latitude=40.7440,
        longitude=-23.0289,
        depth=15.1,
        event_time="2026-06-30T08:30:00"
        )

    assert earthquake_c != earthquake_d


def test_str_representation():
    """
    Test that key attributes of the Earthquake object show up in the output
    """
    earthquake_string = Earthquake(
        magnitude=8.1,
        location="New Jersey",
        latitude=40.7441,
        longitude=-23.0289,
        depth=15.1,
        event_time="2026-06-30T08:30:00"
        )

    text = str(earthquake_string)

    assert "8.1" in text
    assert "New Jersey" in text
    assert "40.7441" in text
    assert "23.0289" in text
    assert "15.1" in text
    assert "2026-06-30 08:30:00" in text
    assert "Great" in text
