import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


def create_box_and_strip_plots(df, metric, save_dir):
    """
    Creates a boxplot and a stripplot for the given metric grouped by 'Group',
    and saves the resulting plot as an image.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        metric (str): The column name for the metric to plot.
        save_dir (str): The directory to save the plot.

    Returns:
        None
    """
    # Set up the figure size for the plot
    plt.figure(figsize=(10, 6))
    # Create a boxplot with orange color
    sns.boxplot(x="Group", y=metric, data=df, color="orange")
    # Overlay a stripplot with black points
    sns.stripplot(x="Group", y=metric, data=df, color="black", alpha=0.25, size=3)
    # Set the title for the plot
    plt.title(f"{metric} Distribution by Group")
    # Save the figure to the specified directory
    plt.savefig(f"{save_dir}/{metric}_boxplot.png", dpi=300)
    # Close the plot to free memory
    plt.close()


def create_kde_plots(df, metric, save_dir):
    """
    Creates a KDE plot for the given metric grouped by 'Group',
    and saves the resulting plot as an image.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        metric (str): The column name for the metric to plot.
        save_dir (str): The directory to save the plot.

    Returns:
        None
    """
    # Set up the figure size for the plot
    plt.figure(figsize=(10, 6))
    # Generate a KDE plot for each group in the 'Group' column
    for group in df["Group"].unique():
        group_data = df[df["Group"] == group][metric]
        sns.kdeplot(data=group_data, label=group, fill=True)
    # Set plot title and axis labels
    plt.title(f"{metric} Distribution by Group")
    plt.xlabel(metric)
    plt.ylabel("Density")
    # Add a legend to the plot
    plt.legend()
    # Save the figure to the specified directory
    plt.savefig(f"{save_dir}/{metric}_kde.png", dpi=300)
    # Close the plot to free memory
    plt.close()


def visualize_analysis_results(save_dir, metrics):
    """
    Visualizes group comparison results from saved CSV files by generating bar charts.

    Parameters:
        save_dir (str): The directory containing the saved CSV files.
        metrics (list): A list of metric names corresponding to the CSV files.

    Returns:
        None
    """
    print("Visualizing analysis results")
    for metric in metrics:
        # Construct the file path for the comparison CSV
        csv_file = os.path.join(save_dir, f"{metric}_group_comparison.csv")
        if os.path.exists(csv_file):
            # Load the CSV file into a DataFrame
            df_stats = pd.read_csv(csv_file)

            # Set 'Group' as the index for plotting
            df_stats.set_index("Group", inplace=True)

            # Create a bar chart for the comparison results
            plt.figure(figsize=(10, 6))
            df_stats.plot(kind="bar")
            plt.title(f"Comparison Results for {metric}")
            plt.xlabel("Group")
            plt.ylabel("Values")
            plt.xticks(rotation=0)

            # Adjust layout to prevent label cutoff
            plt.tight_layout()

            # Save the figure to the specified directory
            plt.savefig(os.path.join(save_dir, f"{metric}_analysis_comparison.png"))
            # Close the plot to free memory
            plt.close()
        else:
            # Print a message if the CSV file is not found
            print(f"No data found for {metric}")


def visualize_group_data(df, analysis_dir="analysis", save_dir="plots"):
    """
    Generates and saves visualizations for group comparisons and metrics distributions.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        analysis_dir (str): The directory containing saved analysis results.
        save_dir (str): The directory to save the visualizations.

    Returns:
        None
    """
    print("Starting data visualization")
    # Ensure the save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # List of metrics to visualize
    metrics = ["eTIV", "nWBV", "ASF"]
    for metric in metrics:
        # Create and save box and strip plots for the metric
        create_box_and_strip_plots(df, metric, save_dir)
        # Create and save KDE plots for the metric
        create_kde_plots(df, metric, save_dir)

    # Visualize group comparison results from the analysis directory
    visualize_analysis_results(analysis_dir, metrics)

    print("Data visualization completed")
