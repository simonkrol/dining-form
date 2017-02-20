import requests



url = 'http://dining.carleton.ca/locations/fresh-food-company/' # Set destination URL here
post_fields = {
	'input_1.3': 'Request Payload',
	'input_1.6': 'Redstone',
	'input_2': 'Warlock',
	'input_3': '100000000',
	'input_4': '6131000000',
	'input_5': 'redstonewarlock@gmail.com',
	'input_6': '02/01/2017',
	'input_15': 'Lunch',
	'input_16': 'Fruit cup',
	'input_17': 'Orange Juice',
	'input_18': 'Caesar',
	'input_19': 'Corn Beef',
	'input_20': 'Granola Bar',
	'is_submit_3': '',
	'gform_submit': '1',
	'gform_unique_id': '3',
	'state_3': '',
	'gform_target_page_number_3': 'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0=',
	'gform_source_page_number_3': '0',
	'gform_field_values': '1'
}     # Set POST fields here

headers = { 
	'Connection': 'Keep-Alive',
	'Content-Encoding': 'gzip',
	'Content-Length': '20',
	'Content-Type': 'text/html'
}

r=requests.post(url, files=post_fields)
#print(r.request.headers)
#print(r.request.file)	
#prepared=r.request
#s=requests.Session()
#s.send(prepared)