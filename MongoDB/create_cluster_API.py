import requests
import json
import base64

# Set your Atlas API credentials
# public_key = 'klycmyfe'
# private_key = '71e2b2e5-ccf6-4573-aa64-4fbffab4b996'

public_key = 'vddavivu'
private_key = '56c8dead-b801-4ddc-8559-3c9e3041ba47'
api_key = '{}:{}'.format(public_key, private_key)
encoded_api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

# Set the Atlas API endpoint and the group ID
url = 'https://cloud.mongodb.com/api/atlas/v2/groups/6434fb5a2ad3f6305bf1bbb3/clusters'
group_id = '6434fb5a2ad3f6305bf1bbb3'

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic {}'.format(encoded_api_key)
}

# Set the payload for the API request
payload = {
    "name": "my-cluster",
    "mongoDBVersion": "4.2",
    "numShards": 3,
    "providerSettings": {
        "providerName": "AWS",
        "regionName": "us-east-1",
        "instanceSizeName": "M10",
        "diskIOPS": 2000,
        "encryptEBSVolume": True
    },
    "backupEnabled": True,
    "autoScaling": {
        "compute": {
            "enabled": True,
            "scaleDownEnabled": True,
            "minInstanceSize": "M10",
            "maxInstanceSize": "M20"
        }
    }
}

# Make the API request to create the cluster
response = requests.post(url.format(group_id), headers=headers, data=json.dumps(payload))

# Check the response status code
if response.status_code == 201:
    print('Successfully created a new MongoDB cluster on Atlas')
else:
    print('Failed to create a new MongoDB cluster on Atlas')
    print(response.content)




# import requests
# import json
# import base64

# # # Set your Atlas API credentials
# # public_key = 'YOUR_PUBLIC_KEY'
# # private_key = 'YOUR_PRIVATE_KEY'
# # api_key = '{}:{}'.format(public_key, private_key)
# # encoded_api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

# # Set the Atlas API endpoint and the project name
# url = 'https://cloud.mongodb.com/api/atlas/v1.0/groups/byName/{}'
# project_name = 'my-project'

# # Set the headers for the API request
# headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     'Authorization': 'Basic {}'.format(encoded_api_key)
# }

# print(url.format(project_name))
# print(headers)

# # Make the API request to retrieve the group ID
# response = requests.get(url.format(project_name), headers=headers)



# # Check the response status code
# if response.status_code == 200:
#     group_id = response.json()['id']
#     print('The group ID for {} is {}'.format(project_name, group_id))
# else:
#     print('Failed to retrieve the group ID for {}'.format(project_name))
#     print(response.content)