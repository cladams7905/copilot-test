# Use falconpy sensors api library to get a list of all sensors.
# 1. import the necessary library from falconpy.
# 2. Query the CrowdStrike Falcon API for sensor data. Call the query_sensors method to get all sensors.
# 3. Inside the method, pass in the last_behavior and first_behavior filters and sort the results in descending order.

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = 'FbMYxe9GgprDTNvUhS3075Zi1HtfI2sQ46dWE8jw'
BASE_URL = 'https://api.us-2.crowdstrike.com'

#Import necessary libraries from falconpy
from falconpy import Hosts

# fetch_data function to return response from CrowdStrike Falcon API
def fetch_data():
    falcon = Hosts(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)
    response = falcon.query_devices(filter="last_behavior:<='2024-09-20'+first_behavior:>='2024-08-05'",
                                    sort="last_behavior|desc")
    return response['body']['resources']

# Main function
def main():
    data = fetch_data()
    if data is None:
        print('No sensors found')
        return
    else:
        print(data)

# call main function
main()