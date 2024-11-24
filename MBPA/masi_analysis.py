import pandas as pd
import numpy as np
import os


# MASI Analysis function
def masi_analysis(input_file_path, output_directory, id_column, selected_columns=None, epsilon=1e-5,
                  data_result_filename="MASI_data_result.csv"):
    # Read data
    DATA = pd.read_csv(input_file_path)  # First row is treated as column names, first column is not treated as an index

    # Ensure ID column exists in the dataframe
    if id_column not in DATA.columns:
        raise ValueError(f"The specified ID column '{id_column}' does not exist in the input data.")

    # Set columns to normalize (analyze)
    if selected_columns is None:
        selected_columns = [col for col in DATA.columns if
                            col != id_column]  # Use all columns except ID column if not specified

    # Drop NA values only for the selected columns (not the whole dataframe)
    DATA = DATA.dropna(subset=selected_columns)

    # Add the CID (ID) column to the data
    DATA['CID'] = DATA[id_column]

    # 1. Data Standardization (Z-score normalization)
    def z_score_standardize(x, mu, sigma, epsilon):
        return (x - mu) / (sigma + epsilon)

    # Standardize the selected columns
    for col in selected_columns:
        mu = DATA[col].mean()
        sigma = DATA[col].std()
        DATA[col] = z_score_standardize(DATA[col], mu, sigma, epsilon)

    # 2. Find the most specific feature for each sample
    DATA['MASI_Feature'] = DATA[selected_columns].idxmax(axis=1)

    # 3. Calculate MASI score for each sample and each feature
    def calculate_masi_score(row, selected_columns, epsilon):
        most_specific_feature = row['MASI_Feature']
        other_features = [col for col in selected_columns if col != most_specific_feature]
        mean_other_features = row[other_features].mean()
        std_other_features = row[other_features].std()
        masi_score = (row[most_specific_feature] - mean_other_features) / (std_other_features + epsilon)
        return masi_score

    # Calculate MASI scores for each row
    DATA['MASI_Feature_Index'] = DATA.apply(lambda row: calculate_masi_score(row, selected_columns, epsilon), axis=1)

    # 4. Normalize the MASI scores
    masi_scores = DATA['MASI_Feature_Index']
    masi_scores_min = masi_scores.min()
    masi_scores_max = masi_scores.max()
    DATA['Normalized_MASI_Feature_Index'] = (masi_scores - masi_scores_min) / (masi_scores_max - masi_scores_min)

    # 5. Calculate MASI scores for each individual feature and add to the dataframe
    for col in selected_columns:
        DATA[f'MASI_Index_{col}'] = DATA.apply(lambda row: calculate_masi_score(row, selected_columns, epsilon), axis=1)

    # Output file path
    output_file_path_data_result = os.path.join(output_directory, data_result_filename)

    # Save the results to a CSV file
    DATA.to_csv(output_file_path_data_result, index=False)

    return {"MASI_result_path": output_file_path_data_result}


# Running the MASI Analysis
def run_masi_analysis():
    input_file_path = "C:/Users/A/Desktop/Bioactive/bioactivate.csv"  # Input file path
    output_directory = "C:/Users/A/Desktop/Bioactive"  # Output directory

    # Specify ID column and columns to analyze
    id_column = "cid"  # ID column
    masi_columns = ["Nontox", "Anti-P. gingivalis", "Hydrogel"]  # Selected columns for analysis

    # Run MASI analysis
    result = masi_analysis(
        input_file_path=input_file_path,
        output_directory=output_directory,
        id_column=id_column,
        selected_columns=masi_columns,  # List of columns to analyze
        epsilon=1e-5,  # Small constant for Z-score normalization
        data_result_filename="MASI_result.csv"  # Output filename for the results
    )

    print(f"MASI analysis results saved at: {result['MASI_result_path']}")


if __name__ == "__main__":
    run_masi_analysis()
