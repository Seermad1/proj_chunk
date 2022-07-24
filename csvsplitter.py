# import os
# import pandas as pd   


# file_name = "books.csv"
# index = 0
# for chunk in pd.read_csv(file_name, chunksize=1000):
#     chunk.to_csv('files/chunk{}.csv'.format(index), index=False)
#     index += 1

import os
import pandas as pd
import math

def csv_split(filename, user_specified_size):
    accepted_fmt = ["json", "csv"]
    doc_name, extension = filename.split(".")[0], filename.split(".")[1]
    """checking if file is an accepted fmt"""
    if extension not in accepted_fmt:
        raise TypeError("Sorry input a an accepted format json or csv file")
    elif extension == "csv":
        size_of_file = os.path.getsize(filename)
        chunk_file_size = math.ceil(size_of_file / user_specified_size)
        total_lenght_of_file = len(pd.read_csv(filename).index)
        row_per_file = math.ceil(total_lenght_of_file / chunk_file_size)
        num = 1
        for each_file in pd.read_csv(filename, chunksize=row_per_file, header=None):
            each_file.to_csv(f"{doc_name}{num}.csv")
            num += 1
        return

csv_split("small_books.csv", 1024)