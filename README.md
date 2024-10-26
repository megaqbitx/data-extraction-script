# Data Extraction Script

This is a Python script designed to extract data from unstructured text files and convert it into a structured format, such as JSON. It is especially useful for processing health-related information, such as patient data and medical records.

## Features

- Extracts key information from text files.
- Organizes data into a structured format (JSON).

## Requirements

- Python 3.x

## Example Input

Page 2 - Position (x: 63.12, y: 752.16): ©WellCare 2022
Page 2 - Position (x: 438.72, y: 752.16): NA2WCMLTR10012E_0000

Page 3 of 12
Page 3 - Position (x: 88.72, y: 101.33): Created:
Page 3 - Position (x: 178.95, y: 101.43): Last
Page 3 - Position (x: 178.95, y: 108.91): Revision:
Page 3 - Position (x: 294.57, y: 101.33): Not Signed:
Page 3 - Position (x: 88.72, y: 116.28): September 5, 2024 10:42
Page 3 - Position (x: 88.72, y: 123.75): AM
Page 3 - Position (x: 294.57, y: 116.28): Sosa, Rosairene (September 5, 2024 10:42
Page 3 - Position (x: 294.57, y: 123.75): AM)
Page 3 - Position (x: 88.72, y: 138.49): Name:
Page 3 - Position (x: 178.95, y: 138.49): Date of Birth:
Page 3 - Position (x: 224.98, y: 138.49): Medicare Number:

## Example Output

{
      "Date of Birth": "09/13/1942",
      "Created": "September 5, 2024 10:42 AM",
      "Name": "dosa, Rosairene",
      "Not Signed": "dosa, Rosairene (September 8, 2024 12:42 PM)",
      "Medicare Number": "asd5T73TK74"
}
