# Use falconpy SpotlightVulnerabilities api library to get a list of all vulnerabilities from the past month.
# 1. import the necessary library from falconpy.
# 2. Query the CrowdStrike Falcon API for incident data. Call the query_vulnerabilities method to get all incidents from the past month.
# 3. Inside the method, pass in the last_behavior and first_behavior filters and sort the results in descending order.

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = 'FbMYxe9GgprDTNvUhS3075Zi1HtfI2sQ46dWE8jw'
BASE_URL = 'https://api.us-2.crowdstrike.com'

#Import necessary libraries from falconpy
from falconpy import SpotlightVulnerabilities

# fetch_data function to return response from CrowdStrike Falcon API
def fetch_data():
    # Create an instance of the SpotlightVulnerabilities class
    vuln = SpotlightVulnerabilities(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    # Call the get_vulnerabilities method to get all vulnerabilities from the past month
    response = vuln.query_vulnerabilities(parameters={"sort": "last_behavior", "filter": f"last_behavior:[now-30d TO now] AND first_behavior:[now-30d TO now]"})
    return response

# Main function
def main():
    # Call the fetch_data function
    response = fetch_data()
    # Output the response
    print(response)

# call main function
main()