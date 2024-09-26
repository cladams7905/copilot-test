# Call this Microsoft 365 API to query advanced hunting data. Search for DeviceProcessEvents of powershell.exe file executions.
# https://api-eu3.securitycenter.microsoft.com/api/advancedhunting/run

# Constants
TENANT_ID = '08ccf1d4-a04c-4f46-8a71-ddd188f2c16b'
CLIENT_ID = 'a6276dfd-6363-40c9-87f3-6895a2b9683e'
CLIENT_SECRET = ''
SCOPE = 'https://api.securitycenter.microsoft.com/.default'
TOKEN_URL = 'https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token'

#Import necessary libraries
import requests

# Create the body for the POST request to get the token
data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': SCOPE
}

# Get the token
def get_token():
    response = requests.post(TOKEN_URL, data=data)
    return response.json()


# Make the API request
url = 'https://api-eu3.securitycenter.microsoft.com/api/advancedhunting/run'
token = get_token()
headers = {
    'Authorization': f'Bearer {token}'
}
response = requests.post(url, headers=headers, json={
    'Query': 'DeviceProcessEvents | where FileName == "powershell.exe"'
})

# Output the response
print(response.json())