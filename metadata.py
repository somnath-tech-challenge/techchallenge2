import requests
import json

# Function to get the json data and printing the keys for selection by user/
def get_instance_meta():
    meta_url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    session = requests.Session()
    result = requests.get(meta_url)
    response_json = result.json()
    for key in response_json.keys():
        print (key)

    return(response_json)

# Function to  retrive the value of the key selected by user.
def get_key_value(meta_json,key):
    meta = meta_json.get(key)
    return(meta)

# The main function to call the two functions and feting input from user.
if __name__ == '__main__':
    meta_json = get_instance_meta()
    key = raw_input("Please enter the Key you want to retrieve: ")
    output = get_key_value(meta_json,key)
    print(output)
