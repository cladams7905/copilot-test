# Use falconpy Detects api library to get a list of all detections from the past month.
# 1. import the necessary library from falconpy.
# 2. declare a fetch_data function that will return the response from the CrowdStrike Falcon API.
# 3. Within the fetch_data function, declare a falcon object using the falconpy library and pass in the client_id and client_secret (i.e. falcon = Detects(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)).
# 4. Use the falcon object to query the CrowdStrike Falcon API for data (e.g. detections, hosts, etc.). Call the query_detects method to get all detections from the past month. Pass in the last_behavior and first_behavior filters to get detections from the past month. Sort the results in descending order.
# 5. If the response status code is 200 and there are resources in the response body dict object can be accessed with ["body"]["resources"], then fetch additional data using get_detect_summaries, passing in the previous query's response body.
# 6. Return the fetched data.
# 7. In the main function, call the fetch_data function and print the response if it is not None.

# Constants
CLIENT_ID = 'd09973764f7946dc9f1b40cebbac1f76'
CLIENT_SECRET = ''
BASE_URL = 'https://api.us-2.crowdstrike.com'

#Import necessary libraries from falconpy
from falconpy import Detects

# fetch_data function to return response from CrowdStrike Falcon API
def fetch_data():
    falcon = Detects(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)
    response = falcon.query_detects(filter="last_behavior:<='2024-09-20'+first_behavior:>='2024-08-05'",
                                    sort="last_behavior|desc")
    results = falcon.get_detect_summaries(ids=response["body"]["resources"])
    return results["body"]["resources"]

# Main function
def main():
    data = fetch_data()
    if data is None:
        print('No detections found')
        return
    else:
        print(data)

# call main function
main()