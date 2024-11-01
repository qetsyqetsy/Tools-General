# Script para exportar todos los títulos de un determinado tipo de archivo (en un directorio específico) a un .txt (en el mismo directorio donde se corre el script)

import os
from tqdm import tqdm  # Ensure tqdm is imported for the progress bar

def extract_titles(folder_path, filetypes, output_file="file_titles.txt"):
    # Debug: Print the folder path being checked
    print(f"Checking folder path: {folder_path}")

    # Check if folder exists
    if not os.path.isdir(folder_path):
        print("The specified folder path does not exist.")
        return

    titles = []

    # Collect all file paths first to get a total count for debugging
    all_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in filetypes):
                all_files.append((root, file))

    # Debug: Check number of files found
    print(f"Debug: Found {len(all_files)} files matching the criteria.")

    # If no files match, print a message and exit
    if not all_files:
        print("No matching files found in the specified folder.")
        return

    # Extract titles from the list of files with a progress bar
    print("Starting extraction...")
    for root, file in tqdm(all_files, desc="Extracting titles", unit="file"):
        title, _ = os.path.splitext(file)
        titles.append(title)
    
    # Write titles to the output file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as f:
        for title in titles:
            f.write(f"{title}\n")

    print(f"Titles extracted and saved to '{output_file}'.")

# Example Usage
folder_path = "J:"  # Update with your actual folder path
filetypes = [".pdf"]  # Add any file extensions you want to search for
output_file = "pdf_titles.txt"  # Optional: name of the output file

extract_titles(folder_path, filetypes, output_file)
