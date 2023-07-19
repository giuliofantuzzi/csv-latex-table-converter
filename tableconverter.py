#-----------------------------------------------------------------------------
# If not already installed
# pip install pandas
# pip install tabulate
#-----------------------------------------------------------------------------
import pandas as pd
from tabulate import tabulate

def csv_to_latex(csv_file, output_file):
    # Read CSV file using pandas
    df = pd.read_csv(csv_file)
    # Convert DataFrame to LaTeX table.
    latex_table = tabulate(df, tablefmt="latex", headers="keys", showindex=False)
    # Save table as a .tex output file
    with open(output_file, "w") as f:
        f.write(latex_table)

#-----------------------------------------------------------------------------
# Replace "input.csv" with the path of the CSV to convert
input_csv_file = "input.csv"

# Replace "output.csv" with the path where to save the .tex file
output_latex_file = "output.tex"

csv_to_latex(input_csv_file, output_latex_file)
#-----------------------------------------------------------------------------
