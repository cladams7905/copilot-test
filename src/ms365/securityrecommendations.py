# Call this Microsoft 365 API to get a list of all security recommendations from the past month.
# https://api-eu3.securitycenter.microsoft.com/api/recommendations

# Constants
TENANT_ID = '08ccf1d4-a04c-4f46-8a71-ddd188f2c16b'
CLIENT_ID = 'a6276dfd-6363-40c9-87f3-6895a2b9683e'
CLIENT_SECRET = 'Nhd8Q~~UvcdsK0eG2AlHNLZ5u2qToy3Mc0.pha8_'
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

# Get the token from posting to the token url and returning the response.access_token
def get_token():
    response = requests.post(TOKEN_URL, data=data)
    return response.json()

# Define the API endpoint and headers
url = 'https://api-eu3.securitycenter.microsoft.com/api/recommendations'
token = get_token()
headers = {
    'Authorization': f'Bearer {token}'
}

# Make the API request
response = requests.get(url, headers=headers)

# Output the response
print(response.json())
