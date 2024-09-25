import pandas as pd
import re

# Data Scrubber Function
def scrub_data(df):
    # Remove unwanted characters from 'Premise Name' and apply proper case
    df['Premise Name'] = df['Premise Name'].apply(lambda x: re.sub(r'[.,|\'´]', '', str(x)).title())

    # Replace street abbreviations and cardinal directions in 'Address Line 1'
    street_abbreviations = {
        'St': 'Street', 'Rd': 'Road', 'Ave': 'Avenue', 'Blvd': 'Boulevard', 'Ste': 'Suite',
        'Ct': 'Court', 'Pkwy': 'Parkway'
    }
    cardinal_directions = {
        r'\bN\b': 'North', r'\bS\b': 'South', r'\bE\b': 'East', r'\bW\b': 'West'
    }

    def replace_abbreviations_and_directions(address):
        # Replace street abbreviations
        for abbr, full in street_abbreviations.items():
            address = re.sub(rf'\b{abbr}\b', full, address)
        # Replace cardinal directions
        for abbr, full in cardinal_directions.items():
            address = re.sub(abbr, full, address)
        return address

    df['Address Line 1'] = df['Address Line 1'].apply(lambda x: replace_abbreviations_and_directions(str(x)))

    return df

# Main function to read, scrub, and save the data
def main():
    # Read the test file (replace 'test_file.xlsx' with your actual file)
    input_file = 'test_file.xlsx'
    output_file = 'cleaned_file.xlsx'

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Scrub the data
    df_cleaned = scrub_data(df)

    # Save the cleaned data to a new Excel file
    df_cleaned.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Data has been scrubbed and saved to {output_file}")

# Run the script
if __name__ == '__main__':
    main()
