import requests
import json
from pprint import *
import os

def get_token_IMDS(resource):
    url = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource={}".format(resource)

    headers = {
        'Metadata': 'true'
    }
    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)['access_token']

def get_adb_cluster(adb_org_id, adb_token, mgmt_token, adb_resource_id):
    url = "https://adb-{}.azuredatabricks.net/api/2.0/clusters/list".format(adb_org_id)
    headers = {
        'Authorization': 'Bearer {}'.format(adb_token),
        'X-Databricks-Azure-SP-Management-Token': mgmt_token,
        'X-Databricks-Azure-Workspace-Resource-Id': adb_resource_id
    }
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)

if __name__ == "__main__":
    adb_org_id = os.getenv('ADB_ORG_ID')
    adb_resource_id = os.getenv('ADB_RESOURCE_ID')
    
    pprint(get_adb_cluster(adb_org_id, get_token_IMDS("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"), get_token_IMDS("https%3A%2F%2Fmanagement.core.windows.net%2F"), adb_resource_id))