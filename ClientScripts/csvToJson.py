import csv
import json

INPUT_SIZE = 10

# Function to convert a CSV to JSON
def make_json(csvFilePath, jsonFilePath):
     
    data = {}
    transactions = []
    id = 1
    i=0
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
         
        for rows in reader:
            transactions.append(rows)
            i += 1
            if i >= INPUT_SIZE:
                break
        data["transactions"] = transactions
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
 
# Call the make_json function
make_json("V:/Documents/Uni/Year 3/Project/Fraud_Detection_Dataset.csv", "outputJson.json")