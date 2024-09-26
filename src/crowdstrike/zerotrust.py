# Use falconpy ZeroTrustAssessment api library to get a list of all incidents from the past month.
# 1. import the necessary library from falconpy.
# 2. Query the CrowdStrike Falcon API for zero trust assessment data. Call the get_assessments method to get all incidents from the past month.

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = 'FbMYxe9GgprDTNvUhS3075Zi1HtfI2sQ46dWE8jw'
BASE_URL = 'https://api.us-2.crowdstrike.com'

#Import necessary libraries from falconpy
from falconpy import ZeroTrustAssessment

# fetch_data function to return response from CrowdStrike Falcon API
def fetch_data():
    # Create an instance of ZeroTrustAssessment
    zta = ZeroTrustAssessment( client_id=CLIENT_ID, client_secret=CLIENT_SECRET, base_url=BASE_URL )

    # Get all incidents from the past month
    response = zta.get_assessment( parameters={ 'created_after': '2021-08-01T00:00:00Z' } )

    return response

# Main function
def main():
    # Call fetch_data function to get response from CrowdStrike Falcon API
    response = fetch_data()

    # Print response
    print( response )

# call main function
if __name__ == '__main__':
    main()