#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csvfile:
            csvreading = csv.DictReader(csvfile)
            data = [i for i in csvreading]
        
        with open("data.json", mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
        
        return True

    except FileNotFoundError:
        return False

    except Exception as e:
        return False
