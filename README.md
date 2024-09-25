# Data Scrubber Script

## Overview

This Python script is designed to clean and standardize Excel data by scrubbing unwanted characters from **Premise Name** fields and replacing common street abbreviations and cardinal directions in **Address Line 1** fields. The script works with any Excel file and can easily be modified for various data-cleaning needs.

## Features

- Cleans up **Premise Name** field by removing:
  - Periods, commas, vertical bars (`|`), apostrophes, and accented characters
  - Converts all text to proper case (e.g., "ABC LLC" becomes "Abc Llc")
- Replaces street abbreviations in the **Address Line 1** field:
  - `St` → `Street`
  - `Rd` → `Road`
  - `Ave` → `Avenue`
  - `Blvd` → `Boulevard`
  - `Ste` → `Suite`
  - `Ct` → `Court`
  - `Pkwy` → `Parkway`
- Replaces cardinal direction abbreviations in the **Address Line 1** field:
  - `N` → `North`
  - `S` → `South`
  - `E` → `East`
  - `W` → `West`
    
 ## Usage

	1.	Prepare the Excel File:
	•	Ensure your data file is in Excel format (.xlsx) and contains columns named Premise Name and Address Line 1.
	2.	Place the Script and Excel File:
	•	Place your Excel file and the Python script in the same directory.
	•	The script expects the file to be named test_file.xlsx. You can change the file name in the script if needed.
	3.	Run the Script:
	•	Execute the Python script. It will read the test_file.xlsx file, scrub the Premise Name and Address Line 1 columns, and generate a cleaned file named cleaned_data.xlsx.
	4.	Output:
	•	The cleaned data will be saved to a new Excel file (cleaned_data.xlsx) in the same directory.
  
## Requirements

- **Python 3.x**
- **pandas**
- **openpyxl**

To install the required libraries, run:
```bash
pip install pandas openpyxl

