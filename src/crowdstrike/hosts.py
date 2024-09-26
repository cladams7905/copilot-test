# Use falconpy Incidents api library to get a list of all hosts.
# 1. import the necessary library from falconpy.
# 2. Query the CrowdStrike Falcon API for host data.

import requests
from falconpy import Hosts

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = 'FbMYxe9GgprDTNvUhS3075Zi1HtfI2sQ46dWE8jw'
BASE_URL = 'https://api.us-2.crowdstrike.com'

# Function to get OAuth2 token
def get_token():
    url = f'{BASE_URL}/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def fetch_hosts():
    falcon = Hosts(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)

    hostname = "DESKTOP-6156KKR"

    response = falcon.query_devices_by_filter(
                    filter=f"hostname:'{hostname}*'"
                    )
    return response


# Main function
def main():
    alerts = fetch_hosts()
    if alerts is None:
        print('No alerts found')
        return
    else:
        print(alerts)


if __name__ == '__main__':
    main()