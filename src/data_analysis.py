def compare_groups(df, metric):
    """
    Compares statistical metrics for a given column (metric) across groups.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        metric (str): The name of the column to analyze.

    Returns:
        pd.DataFrame: A DataFrame containing the mean, min, max, and median values
                      of the metric for each group.
    """
    print(f"Comparing groups for {metric}")
    # Group the DataFrame by the "Group" column and calculate statistical metrics
    group_comparison = df.groupby("Group")[metric].agg(["mean", "min", "max", "median"])
    return group_comparison


def save_group_comparisons(df, metrics, save_dir):
    """
    Saves statistical comparisons for a list of metrics into CSV files.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        metrics (list): A list of column names (metrics) to analyze.
        save_dir (str): The directory where the output files should be saved.

    Returns:
        None
    """
    for metric in metrics:
        print(f"Saving comparison data for {metric}")
        # Perform group comparison for the current metric
        stats = compare_groups(df, metric)
        # Save the comparison results as a CSV file in the specified directory
        stats.to_csv(f"{save_dir}/{metric}_group_comparison.csv")
        print(f"Data saved for {metric}")


def main_analysis(df, save_dir="analysis"):
    """
    Conducts detailed data analysis for specified metrics and saves the results.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        save_dir (str): The directory where the analysis results should be saved.

    Returns:
        None
    """
    print("Starting detailed data analysis")
    # List of metrics to analyze
    metrics = ["eTIV", "nWBV", "ASF"]
    # Save group comparisons for the specified metrics
    save_group_comparisons(df, metrics, save_dir)
    print("Data analysis completed successfully")
