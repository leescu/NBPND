import pandas as pd
import numpy as np
import os

# Define the CMAS analysis function
def cmas_analysis(input_file_path, output_directory, id_column='CID', cmas_columns=None, set_weights=False, custom_weights=None, data_result_filename="CMAS_normalized_matrix.csv"):
    # Read data
    DATA = pd.read_csv(input_file_path)  # First row is treated as column names, first column is not treated as an index

    # Set ID column and ensure it's included in the dataframe
    if id_column not in DATA.columns:
        raise ValueError(f"The specified ID column '{id_column}' does not exist in the input data.")

    # Set columns to normalize (analyze)
    if cmas_columns is None:
        cmas_columns = [col for col in DATA.columns if col != id_column]

    # Drop NA values only for the selected columns
    DATA = DATA.dropna(subset=cmas_columns)

    # 1. Data normalization (Min-Max normalization, select all columns except ID column)
    # Apply Min-Max normalization to all selected columns
    def min_max_normalize(x):
        return (x - x.min()) / (x.max() - x.min())

    DATA_normalized = DATA[cmas_columns].apply(min_max_normalize)

    # Rename the columns to add 'CMAS_' prefix
    DATA_normalized.columns = [f'CMAS_{col}' for col in cmas_columns]

    # Add the ID column as the first column to the normalized data frame
    DATA_normalized.insert(0, id_column, DATA[id_column])

    # 2. Calculate the weighted normalized matrix
    # Set weights based on user input
    if set_weights and custom_weights is not None:
        weights = np.array(custom_weights)
        if len(weights) != len(cmas_columns):
            raise ValueError("Length of custom_weights must match the number of features to normalize.")
        if not np.isclose(weights.sum(), 1):
            raise ValueError("The sum of custom_weights must be equal to 1.")
    else:
        # Assume equal weight for each criterion
        weights = np.full(len(cmas_columns), 1 / len(cmas_columns))

    # Apply weights to the normalized data
    DATA_weighted = DATA_normalized.iloc[:, 1:].multiply(weights, axis=1)

    # 3. Calculate ideal and negative-ideal solutions
    ideal_solution = DATA_weighted.max()  # Ideal solution: maximum value for each column
    negative_ideal_solution = DATA_weighted.min()  # Negative-ideal solution: minimum value for each column

    # 4. Calculate the distance of each sample to the ideal and negative-ideal solutions
    dist_to_ideal = DATA_weighted.apply(lambda row: np.sqrt(((row - ideal_solution) ** 2).sum()), axis=1)
    dist_to_negative_ideal = DATA_weighted.apply(lambda row: np.sqrt(((row - negative_ideal_solution) ** 2).sum()), axis=1)

    # 5. Calculate CMAS score
    cmas_score = dist_to_negative_ideal / (dist_to_ideal + dist_to_negative_ideal)

    # 6. Add CMAS_Score and CMAS_Rank to the normalized data frame
    DATA_normalized['CMAS_Score'] = cmas_score
    DATA_normalized = DATA_normalized.sort_values(by='CMAS_Score', ascending=False)
    DATA_normalized['CMAS_Rank'] = range(1, len(DATA_normalized) + 1)

    # Output file paths
    output_file_path_data_result = os.path.join(output_directory, data_result_filename)

    # Save results as CSV files (CID column first, then normalized columns, then score and rank)
    DATA_normalized.to_csv(output_file_path_data_result, index=False)

    # Return output file paths
    return {
        "DATA_result_path": output_file_path_data_result
    }
