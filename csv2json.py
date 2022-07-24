import json
import csv

csv_file = 'small_books.csv'
json_file_name ='small_books.json'

def csv_to_json(csv_file, json_file_name):
    # json_array= []

    # with open(csv_file, encoding="utf-8") as csv_file_handler:
    #     csv_reader = csv.DictReader(csv_file_handler)

    #     for rows in csv_reader:
    #         json_array.append(rows)

    # with open(json_file_name, 'w', encoding="utf-8") as json_file_handler:
    #     json_file_handler.write(json.dumps(json_array, indent=4))

    data_dict  = {}

    with open(csv_file, encoding="utf-8") as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        for rows in csv_reader:
                for index in range(0, len(rows)):
                    key = index
                    data_dict[key] = rows

    with open(json_file_name, 'w', encoding="utf-8") as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))

csv_to_json(csv_file, json_file_name)