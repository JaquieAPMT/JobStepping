if event.getPreviousValue() != None:

	#Get values from RTG (trolley, hoist, latitude, longitude and spreaders)
	
	spreader_tw_unlocked_value = newValue.getValue()
	tag_path = event.getTagPath().toString()
	rtg_name = tag_path.split("/")[3]
	logger = system.util.getLogger('Job Stepping Tag_RTG_TT_Drop (Tag Change)')
	trolley_position = system.tag.read('[default]PTP/asset/RTG/%s/SM/06_Trolley/125_TrolleyPosition' % rtg_name).value
	hoist_position = system.tag.read('[default]PTP/asset/RTG/%s/SM/05_Main Hoist/125_HoistPosition' % rtg_name).value
	latitude = system.tag.read('[default]PTP/asset/RTG/%s/AT/ADP_GPS/latitude' % rtg_name).value
	longitude = system.tag.read('[default]PTP/asset/RTG/%s/AT/ADP_GPS/longitude' % rtg_name).value
	spreader_size_20 = system.tag.read('[default]PTP/asset/RTG/%s/SM/30_Spreader/386_SpreaderSize20' % rtg_name).value
	spreader_size_40 = system.tag.read('[default]PTP/asset/RTG/%s/SM/30_Spreader/386_SpreaderSize40' % rtg_name).value
	spreader_size_45 = system.tag.read('[default]PTP/asset/RTG/%s/SM/30_Spreader/386_SpreaderSize45' % rtg_name).value
	spreader_size_twin = system.tag.read('[default]PTP/asset/RTG/%s/SM/30_Spreader/386_SpreaderTwinMode' % rtg_name).value

	if spreader_size_20: 
		spreader = '20'
	elif spreader_size_40: 
		spreader = '40'
	elif spreader_size_45:
		spreader = '45'
	elif spreader_size_twin:
		spreader = 'Twin'
	else:
		spreader = 'None'
	
	# Verify if we are doing a drop truck route 
	if spreader_tw_unlocked_value == True and 0 < trolley_position < 3.5 and hoist_position < 7.5 :
		try:
			JobStepping.get_tts_close_to_rtg.main(latitude,longitude,rtg_name,"Drop container",spreader)
		except Exception as e:
			logger.info('Error ejecutando JobSteppingPointInCircle en Tag Change %s'%e)
	# Inside truck route		
	if  spreader_tw_unlocked_value == True and 3.5 < trolley_position < 20:
		try:
			JobStepping.rtg_stack_events.main(rtg_name,trolley_position,hoist_position,"Drop container inside the block",spreader)
		except Exception as e:
			logger.info('Error ejecutando JobSteppingPointInCircle drop cointainer inside the block en Tag Change %s'%e)
		
