#pip install pandas
#pip install tabulate
import pandas as pd
from tabulate import tabulate
def csv_to_latex(csv_file, output_file):
    # Leggo il file CSV utilizzando pandas
    df = pd.read_csv(csv_file)
    # Converto il DataFrame in una tabella LaTeX
    latex_table = tabulate(df, tablefmt="latex", headers="keys", showindex=False)
    # Scrivo la tabella LaTeX nel file di output
    with open(output_file, "w") as f:
        f.write(latex_table)
        
# The user insert as input the csv file to convert
input_csv_file = input('Insert the filepath of the csv file to convert:\n')
# Output file: same filename but change the extension .csv to .tex 
output_latex_file = input_csv_file[0:len(input_csv_file)-4]+".tex"

# Conversion
try:
    csv_to_latex(input_csv_file, output_latex_file)
    conversionmessage= 'Conversion completed successfully!'
    print('-'*len(conversionmessage))
    print(conversionmessage)
    print('-'*len(conversionmessage))
except:
    errormessage= 'Conversion failed!'
    print('-'*len(errormessage))
    print(errormessage)
    print('-'*len(errormessage))


