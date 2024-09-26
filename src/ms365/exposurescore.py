# Call this Microsoft 365 API to get the exposure score.
# https://api-eu3.securitycenter.microsoft.com/api/exposureScore
import requests

# Constants
TENANT_ID = '08ccf1d4-a04c-4f46-8a71-ddd188f2c16b'
CLIENT_ID = 'a6276dfd-6363-40c9-87f3-6895a2b9683e'
CLIENT_SECRET = 'Nhd8Q~~UvcdsK0eG2AlHNLZ5u2qToy3Mc0.pha8_'
SCOPE = 'https://api.securitycenter.microsoft.com/.default'
TOKEN_URL = 'https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token'

# Create the body for the POST request to get the token
data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': SCOPE,
}

#Get the token from posting to the token url and returning the response.access_token
def get_token():
    response = requests.post(TOKEN_URL, data=data)
    print(response)
    return response.json()


# Make the API request
def get_alerts():
    token = get_token()
    print(token)
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get('https://api-eu3.securitycenter.microsoft.com/api/exposureScore', headers=headers)
    return response.json()


# Main function
def main():
    alerts = get_alerts()
    print(alerts)

# Call the main function
main()