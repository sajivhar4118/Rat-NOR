import csv
import os

# Function to process a single CSV and return counts for bottom_right and top_left
def process_csv(file_path):
    bottom_right_counter = 0
    top_left_counter = 0
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip header row
        
        for row in csvreader:
            within_radius_br = row[9].strip().lower() == 'true'  # Check 'within_radius_br'
            within_radius_tl = row[10].strip().lower() == 'true'  # Check 'within_radius_tl'
            
            if within_radius_br:
                bottom_right_counter += 1
            if within_radius_tl:
                top_left_counter += 1
    
    # Divide the counts by 25, as per your requirement
    return bottom_right_counter / 25, top_left_counter / 25

# List of file paths generated in the format Acq{i}_frame_analysis.csv where i is from 1 to 18
csv_files = [f'/projects/b1090/Users/sajiv/frame_csv/Acq{i}_frame_analysis.csv' for i in range(1, 19)]

# Output file for combined results
output_file = '/projects/b1090/Users/sajiv/frame_csv/combined_analysis.csv'

# Prepare the combined CSV file
with open(output_file, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['video', 'bottom_right', 'top_left'])  # Write header
    
    # Process each file and write the results
    for i, csv_file in enumerate(csv_files, start=1):
        if os.path.exists(csv_file):
            bottom_right, top_left = process_csv(csv_file)
            csvwriter.writerow([f'Acq{i}', bottom_right, top_left])
        else:
            print(f"File {csv_file} not found, skipping...")

print(f"Combined analysis complete. Results saved to {output_file}.")
