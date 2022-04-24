import csv
import json

# movie ads
def csv_to_json_1(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding="utf-8") as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(jsonArray, ensure_ascii=False, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/db/ads.csv'
jsonFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/fixtures/ad_old.json'
csv_to_json_1(csvFilePath, jsonFilePath)

# movie categories

def csv_to_json_2(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, ensure_ascii=False, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/db/categories.csv'
jsonFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/fixtures/category_old.json'
csv_to_json_2(csvFilePath, jsonFilePath)

# movie locations

def csv_to_json_3(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, ensure_ascii=False, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/db/locations.csv'
jsonFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/fixtures/location_old.json'
csv_to_json_3(csvFilePath, jsonFilePath)

# movie users
def csv_to_json_4(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, ensure_ascii=False, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/db/users.csv'
jsonFilePath = r'/Users/alexander/Pycharm:Projects/djangoProject/ads/fixtures/users_old.json'
csv_to_json_4(csvFilePath, jsonFilePath)