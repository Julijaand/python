import os
import person_details as pd
import create_dir_file as cdf

pd.personalDetails()
cdf.create_directory()
cdf.create_file()

print("Personal files: ", os.listdir(cdf.directory))

cdf.output_info()