# Use falconpy ScheduledReports api library to get a list of all reports from the past month.
# 1. import the necessary library from falconpy.
# 2. Query the CrowdStrike Falcon API for incident data. Call the get_reports method to get all reports from the past month.

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = ''
BASE_URL = 'https://api.us-2.crowdstrike.com'

#Import necessary libraries from falconpy
from falconpy import ScheduledReports

# fetch_data function to return response from CrowdStrike Falcon API
def fetch_data():
    falcon = ScheduledReports(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)
    response = falcon.get_reports()
    return response['body']['resources']

# Main function
def main():
    data = fetch_data()
    if data is None:
        print('No reports found')
        return
    else:
        print(data)

# call main function
main()