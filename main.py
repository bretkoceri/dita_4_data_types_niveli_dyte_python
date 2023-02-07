# import pathlib

import pathlib
from pathlib import Path

# p = Path(__file__)
# data_path = str(p.cwd())+'\data\\'

# file_input = data_path+'data_input.csv'






import pandas as pd
import streamlit as st

file_input = st.file_uploader('Upload your txt file ')




# data = pd.read_csv(file_input)
# try:
#     data = open(file_input)
    
# except  OSError:
#     print("File not found!")
    

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.write(spectra_df)

data_list = data.readlines()
data_range = len(data_list)
# print(data_range)
for i in range(1,data_range):
    print(i)
    row_read = data_list[i].split(',')
    email_read = row_read[2].split('@')
    try:
        domain_read = email_read[1]
        print(domain_read)
    except:
        print("Error line")
        
    



# with open('data/data_input.csv') as data:
    
#     print(data.readline())
