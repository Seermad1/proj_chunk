import os
import pandas as pd
import math   


file_name = "books.csv"
user_specified_size = 102400
user_specified_number_of_rows = 2000
user_specified_number_of_chunkedfile = 20

file_size = os.path.getsize(file_name)
no_file_row = len(pd.read_csv(file_name))

no_of_chuncked_file = math.floor(file_size/user_specified_size)
chunkedsize_user_specified_number_of_chunkedfiles = math.floor(no_file_row/(user_specified_number_of_chunkedfile-1))
chunksize_user_specified_size = math.floor(no_file_row/no_of_chuncked_file)

index = 0
for chunk in pd.read_csv(file_name, chunksize=chunksize_user_specified_size):
    chunk.to_csv('files/chunk{}.csv'.format(index), index=False)
    index += 1
