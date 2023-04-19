# JobStepping

# Job Stepping tt_close_to_rtg

This script checks for TTs  within a certain radius of a given location and sends the list of TTs to an endpoint via HTTP POST. The script is called by the tagChange function in Ignition, an industrial application platform.

## Requirements

- Python 3.6 or higher
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



