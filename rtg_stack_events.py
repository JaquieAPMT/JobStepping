import json
import system

LOGGER = system.util.getLogger('rtg stack events')

def send_data_to_endpoint(rtg_name, trolley_position, hoist_position, event, spreader):
	"""
	Execute http endpoint http://172.18.125.140:1880/rtgstackevents and send information
	"""
	payload = {
	        "RTG": rtg_name,
	        "TROLLEY POSITION": trolley_position,
	        "HOIST POSITION": hoist_position,
	        "EVENT": event,
	        "SPREADER": spreader
	        }
	
	data = system.util.jsonEncode(payload)
	try:
		client = system.net.httpPost('http://172.18.125.140:1880/rtgstackevents', "application/json",data)
	except Exception as e: 
		LOGGER.info('Problema al enviar informacion al endpoint http://172.18.125.140:1880/rtgstackevents')
	

def main(rtg_name,trolley_position,hoist_position,event,spreader):
	"""
	Method that is called by the tagChange
	"""
	send_data_to_endpoint(rtg_name,trolley_position, hoist_position,event,spreader)
