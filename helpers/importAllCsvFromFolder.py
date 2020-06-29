import glob 
import pandas as pd

def importAllCsvFromFolder(folderPath):
    all_files = glob.glob(folderPath + "/*.csv")

    csv_list = []

    # ratings file is large - ignore for now
    all_files.pop(5)

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, dtype='unicode')
        csv_list.append(df)
    
    return csv_list
