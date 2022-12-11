import requests

def get_instance_meta(key):
    meta_url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    session = requests.Session()
    result = requests.get(meta_url)
    response_json = result.json()
    meta = response_json.get(key)
    return(meta)


if __name__ == '__main__':
    key = raw_input("Please enter the Key you want to retrieve: ")
    output = get_instance_meta(key)
    print(output)
