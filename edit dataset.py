import os
import glob

# Folder containing input files
input_folder = '/Users/chmidnight/Desktop/PAPI_label_YOLO_180824_Edit/labels/'  # Replace with the actual folder path
output_folder = '/Users/chmidnight/Desktop/PAPI_label_YOLO_180824_Edit/Edited/'  # Directory to save the processed files

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get all files from the input folder (adjust file pattern if needed, e.g., '*.txt')
input_files = glob.glob(os.path.join(input_folder, '*'))  # Selects all files in the folder

# Processing each file
for input_file in input_files:
    filtered_lines = []
    
    # Reading the file and processing lines
    with open(input_file, 'r') as file:
        for line in file:
            # Remove lines that start with '2'=PAPI_RED or '4'=PAPI_WHITE
            if not (line.startswith('2') or line.startswith('4')):
                # Replace lines that start with '1'=PAPI_LEFT and '3'=PAPI_RIGHT  to '0'=PAPI
                if line.startswith('1'):
                    filtered_lines.append('0' + line[1:])
                elif line.startswith('3'):
                    filtered_lines.append('0' + line[1:])
                else:
                    filtered_lines.append(line)

    # Save the processed lines to a new file in the output folder
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)

    print(f"Processed file saved as {output_file}")


