import pandas as pd
import os
from data_cleaning import clean_data
from data_analysis import main_analysis
from data_visualization import visualize_group_data


# Main function to orchestrate data analysis workflow
def main():
    """
    This function serves as the entry point for the data analysis pipeline.
    It performs the following steps:
    1. Sets up necessary file paths and directories.
    2. Loads the dataset from a specified file path.
    3. Cleans the data using the `clean_data` function.
    4. Saves the cleaned dataset to a CSV file.
    5. Conducts main analysis using the `main_analysis` function and saves results.
    6. Generates and saves visualizations using `visualize_group_data`.
    """
    print("Starting data analysis")

    # Define the base directory as the directory of the current script
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # Define the path to the dataset
    data_path = os.path.join(base_dir, "..", "data", "dataset.csv")
    # Define directories for saving plots and analysis results
    plots_dir = os.path.join(base_dir, "..", "plots")
    analysis_dir = os.path.join(base_dir, "..", "analysis")

    # Create directories for plots and analysis results if they do not exist
    os.makedirs(plots_dir, exist_ok=True)
    os.makedirs(analysis_dir, exist_ok=True)

    # Load the dataset from the specified path
    df = pd.read_csv(data_path)
    # Check if the dataset is empty or missing
    if df.empty:
        print("Data file is empty or not found.")
        return

    # Clean the dataset using the imported `clean_data` function
    cleaned_df = clean_data(df)
    # Save the cleaned dataset to a new CSV file
    cleaned_df.to_csv(
        os.path.join(base_dir, "..", "data", "cleaned_dataset.csv"), index=False
    )

    # Perform main analysis and save results to the analysis directory
    main_analysis(cleaned_df, save_dir=analysis_dir)
    # Generate visualizations and save them to the plots directory
    visualize_group_data(cleaned_df, analysis_dir, save_dir=plots_dir)

    print("Data analysis completed successfully")


# Run the script only if it is executed directly
if __name__ == "__main__":
    main()
