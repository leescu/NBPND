from cmas_analysis import cmas_analysis

def run_cmas_analysis():
    input_file_path = "C:/Users/A/Desktop/Bioactive/bioactivate.csv"
    output_directory = "C:/Users/A/Desktop/Bioactive"

    # Specify ID column and analysis columns
    id_column = "cid"
    cmas_columns = ["Nontox", "Anti-P. gingivalis", "Hydrogel"]

    # Run CMAS analysis
    result = cmas_analysis(
        input_file_path=input_file_path,
        output_directory=output_directory,
        id_column=id_column,
        cmas_columns=cmas_columns,
        set_weights=False,
        data_result_filename="CMAS_result.csv"  # Custom output file name
    )

    print(f"CMAS analysis results saved at: {result['DATA_result_path']}")

if __name__ == "__main__":
    run_cmas_analysis()
