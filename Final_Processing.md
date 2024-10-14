# Final Data Processing
## Check-Radius

After downloading the CSVs from the Google Colab Notebook, use the following code (also found at [Check-Radius.py]([https://github.com/sajivhar4118/Rat-NOR/blob/main/scripts/Check-Radius.py](https://github.com/sajivhar4118/Rat-NOR/blob/00c20d77bf3dae2047fb13a4b6358e5353b4f542/scripts/Check-Radius.py)). This step combines your DLC and Roboflow data to check if the animal's nose is within a certain distance from each container in each frame.

```python=
import csv
import math

# Function to calculate the Euclidean distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define the radius within which to check
radius = 20.5  # Adjust this value as needed

# File paths
for i in range(1, 19):
    object_coords_csv = f'/projects/b1090/Users/sajiv/frame_csv/video_frames_R{i}.csv'
    rat_nose_csv = f'/projects/b1090/Users/sajiv/NOR/DLC-DATA/NOR/DLC CSVs/NOR10_Acq_R{i}DLC_mobnet_100_ExploreAug18shuffle1_750000.csv'
    output_csv = f'/projects/b1090/Users/sajiv/frame_csv/Acq{i}_frame_analysis.csv'

    # Read the rat nose coordinates from the CSV (starting from the 4th row)
    rat_nose_data = {}
    with open(rat_nose_csv, 'r') as rat_file:
        rat_reader = csv.reader(rat_file)
    
        # Skip the first three rows
        for _ in range(3):
            next(rat_reader)
    
        # Read the remaining rows
        for row in rat_reader:
            try:
                frame_number = int(row[0].strip())
                nose_x = float(row[1].strip())
                nose_y = float(row[2].strip())
                rat_nose_data[frame_number] = (nose_x, nose_y)
            except ValueError:
                print(f"Skipping invalid data in row: {row}")

    # Process the object coordinates and check distances
    with open(object_coords_csv, 'r') as object_file, open(output_csv, 'w', newline='') as output_file:
        object_reader = csv.reader(object_file)
        output_writer = csv.writer(output_file)

        # Write header
        output_writer.writerow(['frame_number', 'br_x', 'br_y', 'tl_x', 'tl_y', 
                            'nose_x', 'nose_y', 'distance_to_br', 'distance_to_tl', 
                            'within_radius_br', 'within_radius_tl'])

        next(object_reader)  # Skip the header

        for row in object_reader:
            try:
                frame_number = int(row[0].strip())
                br_x = float(row[1].strip())
                br_y = float(row[2].strip())
                tl_x = float(row[3].strip())
                tl_y = float(row[4].strip())

                # Get the rat's nose coordinates for this frame
                if frame_number in rat_nose_data:
                    nose_x, nose_y = rat_nose_data[frame_number]

                    # Calculate distances
                    distance_to_br = calculate_distance(br_x, br_y, nose_x, nose_y)
                    distance_to_tl = calculate_distance(tl_x, tl_y, nose_x, nose_y)

                    # Check if within radius
                    within_radius_br = distance_to_br <= radius
                    within_radius_tl = distance_to_tl <= radius

                    # Write the results to the CSV
                    output_writer.writerow([frame_number, br_x, br_y, tl_x, tl_y, 
                                        nose_x, nose_y, distance_to_br, distance_to_tl, 
                                        within_radius_br, within_radius_tl])
            except ValueError:
                print(f'Skipping invalid data in row: {row}')

    print(f"Analysis complete. Results saved to {output_csv}.")
```
## Time Calculation + Data Combining
Then run the following code (Also found [Final-Analysis.py](https://github.com/sajivhar4118/Rat-NOR/blob/00c20d77bf3dae2047fb13a4b6358e5353b4f542/scripts/Final-Analysis.py) to calculate the amount of time the animal spent inspecting each object in each video. THIS IS THE LAST STEP!

```python=
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
```
