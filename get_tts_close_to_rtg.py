import json
import system
from math import radians, sin, cos, sqrt

logger = system.util.getLogger('Job Stepping tt_close_to_rtg')
RADIUS = 50

def point_in_circle(lat1, lon1, lat2, lon2):
	"""
	Check if a point (lat2, lon2) is within a circle of radius (in meters) centered at (lat1, lon1)	
	"""
	lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
	dlat = lat2 - lat1
	dlon = lon2 - lon1
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * sqrt(a)
	distance = 6371000 * c
	return distance <= RADIUS


def find_tt_within_radius(lat1, lon1):
	"""
	Find all TTs located within a given radius (in meters) of a point (lat1, lon1)
	"""
	ruta = '[default]PTP/asset/TT'
	tags = system.tag.browseTags(parentPath=ruta, recursive=True, tagType="OPC", quality ="Good")
	tt_data = [str(tag) for tag in tags if not tag.isFolder() and ("latitude" in str(tag) or "longitude" in str(tag))]
	tt_lat_lon = []
	tt_close_to_rtg = []
	
	for tag in tt_data:
		tt_name = tag.split("/")[3]
		filtred_tt = list(filter(lambda x: tt_name in x, tt_data))
		lat2 = None
		lon2 = None
	
		for tt_signal in filtred_tt:
			if 'latitude' in tt_signal:
				lat2 = tt_signal
			if 'longitude' in tt_signal:
				lon2 = tt_signal
	     
		if lat2 and lon2:
			values = system.tag.readBlocking([lat2, lon2])
			lat2_value = values[0].value
			lon2_value = values[1].value
			tt_lat_lon.append({"name": tt_name, "lat": lat2_value, "lon": lon2_value})
	        
	for tt in tt_lat_lon:
		if point_in_circle(lat1, lon1, tt['lat'], tt['lon']):
			if not tt['name'] in tt_close_to_rtg:
				tt_close_to_rtg.append(tt['name'])
	return tt_close_to_rtg

def send_data_to_endpoint(rtg, event, spreader, tts):
	"""
	Execute http endpoint http://172.18.125.140:1880/rtg and send information
	"""
	payload = {
	        "RTG": rtg,
	        "EVENT": event,
	        "SPREADER": spreader,
	        "TTs": tts
	    }
	data = system.util.jsonEncode(payload)
	try:
		client = system.net.httpPost('http://172.18.125.140:1880/rtg', "application/json",data)
	except Exception as e: 
		logger.info('Error sending data to the endpoint http://172.18.125.140:1880/rtg: %s', str(e))

def main(lat1,lon1,rtg,event,spreader):
    """
    This method is called by the tagChange
    """
    tt_list = find_tt_within_radius(lat1,lon1)
    if len(tt_list) != 0:
    	send_data_to_endpoint(rtg,event,spreader,tt_list)
