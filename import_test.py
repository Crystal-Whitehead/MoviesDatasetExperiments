import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import glob 

from helpers.importAllCsvFromFolder import importAllCsvFromFolder

# file names: credits, keywords, links, ratings, movies_metadata

path = r'./dataset' # use your path

csv_list = importAllCsvFromFolder(path)

frame = pd.concat(csv_list, axis=0, ignore_index=True)

print(frame.head())


 



