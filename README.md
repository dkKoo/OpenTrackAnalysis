# OpenTrack Data Analysis

This Python script analyzes OpenTrack data from multiple CSV files, calculates statistics, and generates visualizations. The analysis results are saved in separate directories for each input file.

## Features

- Loads multiple CSV files using a file dialog
- Calculates statistics (mean, standard deviation, minimum, maximum) for raw and filtered data
- Generates 2D and 3D visualizations of the data
- Saves the statistics and visualizations in separate directories for each input file

## Dependencies

- Python 3.x
- pandas
- matplotlib
- tkinter

## Usage

1. Run the script using a Python interpreter
2. Select the input CSV files using the file dialog
3. Choose the directory where the analysis results will be saved
4. The script will process each input file and save the results in separate directories

## Code Structure

The script consists of two main functions:

1. `analyze_and_save(file_path, save_directory, stats_raw_combined, stats_filtered_combined)`
  - Loads a single CSV file
  - Calculates statistics for raw and filtered data
  - Generates 2D and 3D visualizations
  - Saves the statistics and visualizations in a separate directory for the input file

2. `main()`
  - Prompts the user to select input CSV files and the save directory
  - Initializes the combined statistics dataframes
  - Calls `analyze_and_save()` for each input file
  - Saves the combined statistics as CSV files

## Example Output

The script generates the following output for each input file:

- `filename_plot/` directory containing:
 - `filename_2d_plot.png`: 2D visualization of raw and filtered data
 - `filename_raw_3d_plot.png`: 3D visualization of raw data
 - `filename_filtered_3d_plot.png`: 3D visualization of filtered data

Additionally, the script saves the combined statistics for all input files:

- `stats_raw_combined.csv`: Combined statistics for raw data
- `stats_filtered_combined.csv`: Combined statistics for filtered data
