from masi_analysis import masi_analysis  # Assuming you have imported the MASI function

def run_masi_analysis():
    input_file_path = "C:/Users/A/Desktop/Bioactive/bioactivate.csv"  # Input file path
    output_directory = "C:/Users/A/Desktop/Bioactive"  # Output directory where the results will be saved

    # Specify ID column and analysis columns
    id_column = "cid"  # ID column in the dataset (e.g., sample or molecule ID)
    masi_columns = ["Nontox", "Anti-EBV", "Hydrogel"]  # Selected columns for MASI analysis

    # Run MASI analysis
    result = masi_analysis(
        input_file_path=input_file_path,
        output_directory=output_directory,
        id_column=id_column,
        selected_columns=masi_columns,  # Selected columns to analyze
        epsilon=1e-5,  # Small constant for Z-score normalization
        data_result_filename="MASI_result.csv"  # Custom output file name
    )

    print(f"MASI analysis results saved at: {result['MASI_result_path']}")

if __name__ == "__main__":
    run_masi_analysis()
