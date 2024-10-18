import os

def rename_files_with_leading_zeros(folder_path, total_digits=3):
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            # Extract the number from the filename
            number = filename.split('.')[0]
            
            # Format the number with leading zeros
            new_name = f"{int(number):0{total_digits}}.png"
            
            # Rename the file
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_name)
            )
            print(f"Renamed {filename} to {new_name}")

# Example usage:
folder_path = "path_to_your_folder"
rename_files_with_leading_zeros(folder_path)
