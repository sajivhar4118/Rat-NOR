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
