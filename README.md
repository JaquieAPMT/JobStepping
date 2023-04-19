# JobStepping

# Job Stepping JobStepping/get_tts_close_to_rtg

This script checks for TTs  within a certain radius of a given location and sends the list of TTs to an endpoint via HTTP POST. The script is called by the tagChange function in Ignition, an industrial application platform.

## Requirements
- Ignition platform (for the tagChange function)
- `system` module
- `json` module
- `math` module

## Usage

The `main` function is called by the tagChange function in Ignition. It takes the following arguments:

- `lat1`: latitude of the location to check for TTs
- `lon1`: longitude of the location to check for TTs
- `rtg`: name of the RTG (Rubber Tired Gantry) associated with the event
- `event`: name of the event associated with the TTs (e.g. "Load", "Unload")
- `spreader`: name of the spreader associated with the event

The `find_tt_within_radius` function takes the latitude and longitude of a location as arguments and returns a list of TTs within a certain radius of that location.

The `send_data_to_endpoint` function takes the RTG name, event name, spreader name, and list of TTs as arguments and sends them to an endpoint via HTTP POST.

# RTG Stack Events JobStepping/rtg_stack_events

This script sends data to an endpoint when a tag is changed.

## Dependencies

- Ignition 8.x

## Installation

1. Clone this repository to your local machine.
2. Open Ignition Designer.
3. Create a new Tag Change event.
4. In the Tag Change event script editor, copy and paste the contents of `main.py` into the editor.
5. Replace the values of `rtg_name`, `trolley_position`, `hoist_position`, `event`, and `spreader` with the appropriate tag paths or values for your system.
6. Save and publish the Tag Change event.

## Usage

This script will execute an HTTP POST request to the endpoint `http://172.18.125.140:1880/rtgstackevents` with the following payload:


If the request is successful, the data will be sent to the specified endpoint. If there is an error sending the data, an error message will be logged.

# Tag Change RTG Stack Events TAG_RTG_TT_Drop and TAG_RTG_TT_Lift

This code consists of a set of Python scripts for sending real-time event data from a Rubber Tyred Gantry (RTG) crane to an HTTP endpoint.


## Installation

1. Import the Python modules `JobStepping/get_tts_close_to_rtg.py`, `JobStepping/rtg_stack_events.py` into your Ignition project.

2. Set up a tag change event script that triggers TAG_RTG_TT_xxx module in response to changes in a specific tag. This script requires the previous scripts as dependencies. 

## Usage

The TAG_RTG_TT_xx script is triggered when a specific tag is changed. Upon triggering, it retrieves data from various tags associated with the RTG crane, including trolley and hoist positions, GPS coordinates, and the type of spreader being used. If the spreader is unlocked and the crane is in a specific position, the script sends an HTTP POST request to an external endpoint with the collected data.

## Configuration

The TAG_RTG_TT_xx script can be customized to include additional data points by modifying the script to read from other tags in the Ignition project. Similarly, the HTTP endpoint can be updated to point to a different URL.
