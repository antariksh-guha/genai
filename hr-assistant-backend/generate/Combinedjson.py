import json
import glob

# List of JSON files to merge
json_files = [
    'synthetic_data_marketing.json',
    'synthetic_data_trading.json',
    'synthetic_data_technology.json',
    'synthetic_data_riskmgmt.json',
    'synthetic_data_operations.json'
]

# Initialize an empty list to hold all employee records
all_employees = []

# Read and combine data from all JSON files
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        all_employees.extend(data)

# Sort the combined data by EMP_ID
sorted_employees = sorted(all_employees, key=lambda x: x['EMP_ID'])

# Save the sorted data to a new JSON file
with open('employee.json', 'w') as f:
    json.dump(sorted_employees, f, indent=4)

print("Combined and sorted data saved to employee.json")