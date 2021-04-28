import json
import requests
import glom
import sys


TARGET_KEY = str(sys.argv[1])
TARGET_VALUE = "to_be_replaced"
metadata_url = "http://169.254.169.254/latest/meta-data/"
metadata_dict = {}

## function to created nested dictionary path
def create_path(d, i, list_1):
    if i < len(list_1):
        k = list_1[i]
        if list_1[i] not in d.keys():
            d.update({list_1[i] : {} })
            create_path(d.get(k), i+1, list_1)
        else:
            create_path(d.get(k), i+1, list_1)
    else:
        exit

## function
def get_value(url):
        val = requests.get(url).text
        paths = [x for x in val.splitlines()]
        for i in paths:
                if i[-1] == '/':
                        get_value(url+i)
                else:
                        nested_value = requests.get(url+i).text
                        nested_keys = (url+i).replace(metadata_url,'').split('/')
                        create_path(metadata_dict, 0, nested_keys)
                        glom.assign(metadata_dict, ".".join(nested_keys), nested_value)
                        if i == TARGET_KEY:
                                global TARGET_VALUE
                                TARGET_VALUE = nested_value
                        #print(metadata_dict)
                        #print("==========")

# calling the function
get_value(metadata_url)
#print(metadata_dict)

# saving the dictionary in a file in json format
with open("instance_metadata.json", 'w') as file:
    json_string = json.dumps(metadata_dict,  indent=5)
    file.write(json_string)

if TARGET_VALUE == "to_be_replaced":
        print("Incorrect key")
else:
        print("Target key found")
        print(TARGET_KEY+" : "+TARGET_VALUE)