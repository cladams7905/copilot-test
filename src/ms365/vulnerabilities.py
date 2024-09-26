# Call this Microsoft 365 API to get a list of all vulnerabilities from the past month.
# https://api-eu3.securitycenter.microsoft.com/api/machines

#Import necessary libraries
import requests

# Create the body for the POST request to get the token
data = {
    'grant_type': 'client_credentials',
    'client_id': 'a6276dfd-6363-40c9-87f3-6895a2b9683e',
    'client_secret': '',
    'scope': 'https://api.securitycenter.microsoft.com/.default'
}

# Get the token from posting to the token url and returning the access token from the json response
def get_token():
    response = requests.post('https://login.microsoftonline.com/08ccf1d4-a04c-4f46-8a71-ddd188f2c16b/oauth2/v2.0/token', data=data)
    return response.json()['access_token']

# Define the API endpoint and headers
api_url = "https://api-eu3.securitycenter.microsoft.com/api/vulnerabilities"

# Make the API request
headers = {
    "Authorization": f"Bearer {get_token()}",
    "Content-Type": "application/json"
}

# Output the response
response = requests.get(api_url, headers=headers)

print(response.json())