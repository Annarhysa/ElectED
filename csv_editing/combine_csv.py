import os
import pandas as pd

def combine_csv_files(data_folder, output_file):
    combined_df = pd.DataFrame()

    # Walk through the data directory and read each CSV file
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path, encoding='utf-8')  # Try utf-8 encoding first
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Fall back to ISO-8859-1 if utf-8 fails
                combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)

# Specify the data folder and output file
data_folder = 'data'
output_file = 'data/all.csv'

combine_csv_files(data_folder, output_file)

print(f"Combined CSV files saved to {output_file}")
