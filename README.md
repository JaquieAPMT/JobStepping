# JobStepping

Description
This code defines a Python script that can be called by a tag change event. It reads latitude and longitude data from a set of tags, checks if any of those points are within a certain radius of a specified point, and if so, sends data to an endpoint using HTTP POST request.

Requirements
This script requires the following Python libraries:

json
system
math
Usage
To use this script, call the main function with the following arguments:

lat1: the latitude of the center point of the circle to check for proximity to
lon1: the longitude of the center point of the circle to check for proximity to
rtg: a string representing the RTG identifier
event: a string representing the event identifier
spreader: a string representing the spreader identifier
The find_tt_within_radius function takes lat1 and lon1 as arguments and returns a list of TTs located within the specified radius of the center point. The send_data_to_endpoint function takes rtg, event, spreader, and tts as arguments and sends a JSON payload to a specified endpoint using HTTP POST request.

Notes
The radius of the circle to check proximity to is hardcoded as RADIUS = 50. Change this value to adjust the radius as needed.
The endpoint URL is hardcoded as 'http://172.18.125.140:1880/rtg'. Change this value to adjust the endpoint URL as needed.
This code assumes that the relevant tags are located under the 'default/PTP/asset/TT' path. Change this path in the find_tt_within_radius function if the tags are located elsewhere.
