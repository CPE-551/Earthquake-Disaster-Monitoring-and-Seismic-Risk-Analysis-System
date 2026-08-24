# Earthquake Disaster Monitoring and Seismic Risk Analysis System Using Python

## Team Members

- Kalpana P (kp@stevens.edu)
- Rachel Balji (rbalji1@stevens.edu)
- Tim Clancy (tclancy1@stevens.edu)

## Project Description

Earthquakes are one of the most destructive natural hazards, causing significant damage to buildings, infrastructure, and communities. Engineers, scientists, and emergency management organizations analyze earthquake data to understand seismic activity, identify high risk areas, and support disaster preparedness. However, large earthquake datasets contain raw information that requires processing and analysis to extract meaningful scientific and engineering insights, including prediction analysis.

The proposed project, Earthquake Disaster Monitoring and Seismic Risk Analysis System, will develop a Python-based application that analyzes historical earthquake data to identify seismic activity patterns and provide useful statistical and visual insights. The project will use the publicly available USGS Earthquake Hazards Program Earthquake Catalog dataset, which contains information such as earthquake magnitude, location, geographic coordinates, depth, and occurrence time.

The application will load and validate USGS earthquake data, represent events using object-oriented programming, analyze magnitude, depth, frequency, and geographic patterns, identify significant events using configurable thresholds, and generate statistical summaries and visualizations. The goal of this project is to create a Python-based tool that helps organize and interpret earthquake data for disaster awareness and engineering analysis.

## Data Source

Uses the publicly available USGS Earthquake Hazards Program Earthquake Catalog dataset, which contains information such as earthquake magnitude, location, geographic coordinates, depth, and occurrence time.

Data set file used in this project is data/earthquakes.csv"

## Installation

TO DO

## How to Run 

TO DO

## Project Structure

- **earthquake.py** — This module defines the Earthquake class, which represents a single earthquake event obtained from the United States Geological Survey (USGS) Earthquake Catalog.
- **analyzer.py** — This module contains the EarthquakeAnalyzer class. The class manages multiple Earthquake objects and performs seismic data analysis.
- **data_loader.py** — This module loads earthquake records from a USGS Earthquake Catalog CSV dataset. It validates the required columns and important data fields, converts valid records into Earthquake objects, and returns them as a list.
- **report.py** — This module provides functionality for exporting earthquake risk analysis results to a CSV file.
- **visualization.py** — This module provides visualization functions for earthquake analysis. Matplotlib is used to create graphical representations of earthquake activity, including magnitude distributions, earthquake frequency trends, and relationships between earthquake depth and magnitude.
- **main.py** — Main execution script for the earthquake risk analysis system. Loads the USGS earthquake dataset, converts records into Earthquake objects, performs seismic analysis, generates risk reports, exports results, and creates visualization charts.

## Class Design

The project implements two major classes with a composition relationship.

**Earthquake** represents an individual earthquake event and stores its physical and geographic properties. Attributes: magnitude, location, latitude, longitude, depth, date and time. Methods: store earthquake information, determine earthquake severity category, display earthquake information using `__str__()`, compare earthquake events using `__eq__()`.

**EarthquakeAnalyzer** manages a collection of Earthquake objects and performs statistical analysis, filtering, and risk assessment across multiple earthquake events. Attributes: a list of Earthquake objects, analysis results stored in dictionaries. Methods: calculate average magnitude, find the strongest earthquake events, analyze earthquake frequency, generate risk assessment reports.

The relationship between these classes is based on composition because an EarthquakeAnalyzer object contains and processes multiple Earthquake objects.

## Key Features and Python Concepts Demonstrated

- **Meaningful functions** — `load_earthquake_data()` reads earthquake records from the USGS dataset and converts raw data into usable Python objects. `generate_risk_report()` summarizes earthquake activity, reporting the total number of earthquakes analyzed, average magnitude, highest magnitude event, and number of high-risk earthquakes.
- **Advanced Python libraries** — Pandas is used for reading earthquake CSV files, cleaning and organizing data, and performing statistical analysis. NumPy is used for numerical calculations, computing averages and statistical values. Matplotlib is used for creating earthquake magnitude charts, visualizing earthquake frequency trends, and displaying relationships between depth and magnitude.
- **Exception handling** — The program handles cases where the dataset file does not exist or the file format is incorrect, and validates earthquake records for missing values or invalid magnitude/depth values.
- **Data input and output** — Input consists of earthquake records from the USGS Earthquake Hazards Program Earthquake Catalog dataset. Output includes earthquake analysis reports, statistical summaries, visualization charts, and exported results files, including a CSV summary report and PNG chart files saved to an outputs/ folder.
- **Loops and conditional logic** — Loops are used for processing earthquake records, such as iterating through earthquake events and calculating statistics across multiple regions. Conditional logic is used for earthquake classification.
- **Data types** — Mutable types include list (storing earthquake objects), dictionary (storing regional statistics), and set (storing unique earthquake locations). Immutable types include float (earthquake magnitude and depth), string (location information), and tuple (geographic coordinates).
- **Operator overloading** — `__str__()` provides a readable description of an earthquake object. `__eq__()` compares two earthquake objects based on selected attributes, such as magnitude, location, and occurrence time, enabling meaningful object comparisons.
- **Documentation** — Each module, class, and function includes module header information, proper docstrings, explanation of parameters and return values, and comments describing important program logic.
- **`__name__` entry point** — The project includes an `if __name__ == "__main__":` block in the main program to serve as the application's entry point, allowing the program to be executed directly while also enabling individual modules to be imported and tested independently.
- **List comprehension** — Used to efficiently filter and create collections of earthquake events that meet specified criteria, such as earthquakes above a selected magnitude threshold.
- **Built-in libraries** — Includes datetime for processing earthquake timestamps, os for file handling, and statistics for computing summary statistics where appropriate.
- **Generator function** — A generator function is used to process earthquake records one at a time, improving memory efficiency when working with large datasets.
- **Lambda expressions** — Used with functions such as `max()` to organize and analyze earthquake data based on attributes including magnitude, depth, or occurrence time.

## Testing

Pytest test cases validate that Earthquake objects are created correctly and that EarthquakeAnalyzer accurately calculates statistics such as average magnitude, strongest earthquake, and number of high-risk events.

TO DO


## Output

Output files include a CSV summary report and PNG chart files saved to an outputs/ folder.
