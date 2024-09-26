# Define variables
import requests

tenant_id = "08ccf1d4-a04c-4f46-8a71-ddd188f2c16b"
client_id = "a6276dfd-6363-40c9-87f3-6895a2b9683e"
client_secret = ""
scope = "https://api.securitycenter.microsoft.com/.default"
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Create the body for the POST request to get the token
body = {
    'client_id': client_id,
    'scope': scope,
    'client_secret': client_secret,
    'grant_type': "client_credentials"
}

# Get the token
response = requests.post(token_url, data=body)
token = response.json().get('access_token')

# Define the API endpoint and headers
api_url = "https://api.securitycenter.microsoft.com/api/machines"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.get(api_url, headers=headers)

# Output the response
print(response.json())