import requests



url = 'http://dining.carleton.ca/locations/fresh-food-company/' # Set destination URL here
post_fields = {
	'input_1.3': 'Redstone',
	'input_1.6': 'Warlock',
	'input_2': '100000000',
	'input_3': '6131000000',
	'input_4': 'redstonewarlock@gmail.com',
	'input_5': '02/01/2017',
	'input_6': 'Lunch',
	'input_15': 'Fruit cup',
	'input_16': 'Orange Juice',
	'input_17': 'Caesar',
	'input_18': 'Grilled Cheese',
	'input_19': 'Granola Bar',
	'input_20': 'Text',
	'is_submit_3': '1',
	'gform_submit': '3',
	'gform_unique_id': '',
	'state_3': 'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0=',
	'gform_target_page_number_3': '0',
	'gform_source_page_number_3': '1',
	'gform_field_values':'' 
}     # Set POST fields here

r=requests.post(url, data=post_fields)
