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
  
## Requirements

- **Python 3.x**
- **pandas**
- **openpyxl**

To install the required libraries, run:
```bash
pip install pandas openpyxl
