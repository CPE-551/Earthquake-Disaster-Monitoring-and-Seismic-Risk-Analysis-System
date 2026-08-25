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

Data set file used in this project is data/earthquakes.csv

## Installation

This project uses Python 3.12, 3.13, or 3.14 and was developed using Python 3.14. The following Python packages are required:
-Pandas: used to read and organize the earthquake CSV data.
-NumPy: used for numerical calculations.
-Matplotlib: used to create the earthquake visualizations.
-Pytest: used for testing.
-Jupyter: used to run the main Jupyter Notebook.
-Ipykernel: used to run the main Jupyter Notebook.

**Installing the packages**:
1. Open a terminal in the project directory and run the following command:
python -m pip install pandas numpy matplotlib pytest jupyter ipykernel

If the machine uses the py command, the following can be used:
py -m pip install pandas numpy matplotlib pytest jupyter ipykernel

The main program is main.ipynb. When opening main.ipynb in VS Code, select a Python 3.12, 3.13, or 3.14 krnel that has the required packages installed.

## How to Run 

The main program is main.ipynb.

To run the project in VS Code:
1. Open the project folder in VS Code.
2. Open main.ipynb in Jupyter Notebook.
3. Select the Python 3.12, 3.13, or 3.14 Jupyter kernel.
4. Make sure the required packages have been installed using the installation command above and the dataset is located at data/earthquakes.csv.
5. Run the cells in main.ipynb. The notebook shall load the dataset, create the earthquake objects, perform the analysis, generate the risk report, and create the visualization files.
6. The generated files will be saved in outputs/.

The Jupyter notebook connects the project modules and performs the complete analysis. It loads the earthquake data, creates Earthquake objects, adds the objects to an EarthquakeAnalyzer, performs the analysis, generates the risk report, and creates the visualizations.

The project also includes main.py, which can be run from the project directory using the following commands:
python main.py OR py main.py.

## Project Structure

- **earthquake.py** — This module defines the Earthquake class, which represents a single earthquake event obtained from the United States Geological Survey (USGS) Earthquake Catalog.
- **earthquake_analyzer.py** — This module contains the EarthquakeAnalyzer class. The class manages multiple Earthquake objects and performs seismic data analysis.
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

The project includes Pytest test files for the earthquake class, data loader, and analyzer. The tests cover areas including:
-Creating Earthquake objects.
-Comparing earthquake objects.
-Testing the string representation of an earthquake.
-Handling a missing dataset file.
-Loading a valid earthquake record.
-Handling missing data.
-Testing the earthquake record generator.
-Calculating average magnitude.
-Finding the strongest earthquake.
-Filtering earthquakes by magnitude.
-Analyzing earthquake frequency.
-Generating the risk report.


To run all tests from the Project Directory:

```bash
pytest test_data_loader.py -v
pytest test_analyzer -v
pytest test_earthquake.py -v
```

## Output

Output files include a CSV summary report and PNG chart files saved to an outputs/ folder.


## Team Contributions

### Kalpana P:
- Implemented: `earthquake.py`, `earthquakeanalyzer.py`, `visualization.py`, and `test_analyzer`.
- Refactored or updated: `data_loader.py`, `report.py` (formerly dataprocessing.py)
- Added: earthquake base classes, input validation, analysis functions, visualizations, and unit tests.
- Documented: module, class, and function docstrings; added or updated code comments.

### Rachel Balji:
-Implemented: dataprocessing.py (load_earthquake_data and export_risk_report) and main.ipynb
-Updated: dataloader.py (added iter_earthquake_records), README.md
-Added: dataset processing functions, generator for individual dataset processing

### Tim Clancy:
- Implemented and/or Updated []
- Added: [tests, validation, visualizations]
- Documented
