import os
import shutil
import subprocess

# Define the input and output folders
input_folder = "./stl_models"  
output_folder = "./voxel_models"  

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for file_name in os.listdir(input_folder):
    # Check if the file has an STL extension
    if file_name.lower().endswith('.stl'):
        # Construct the full path to the STL file
        input_file_path = os.path.join(input_folder, file_name)
        
        # Define the output file name (it will be created in the input folder by binvox)
        output_file_name = f"{os.path.splitext(file_name)[0]}.binvox"
        output_file_path_in_input_folder = os.path.join(input_folder, output_file_name)
        
        try:
            # Run the binvox command
            result = subprocess.run(
                ['binvox', '-d', '32', '-e', '-t', 'binvox', input_file_path],
                capture_output=True,
                text=True
            )
            
            # Print the output or error
            if result.returncode == 0:
                print(f"Converted: {file_name} -> {output_file_name}")
                # Move the output file to the voxel_models folder
                shutil.move(output_file_path_in_input_folder, os.path.join(output_folder, output_file_name))
                print(f"Moved: {output_file_name} -> {output_folder}")
            else:
                print(f"Error processing {file_name}: {result.stderr}")

        except FileNotFoundError:
            print("Error: 'binvox' command not found. Ensure it's installed and added to your PATH.")
            break

print("All files have been processed.")
