import requests



url = 'http://dining.carleton.ca/locations/fresh-food-company/' # Set destination URL here
def read_meals():
	infile=open('meals.txt', 'r')
	saved_meals=[]
	meal={}
	#meal={'input_1.3': fname, 'input_1.6': lname, 'input_2': sn, 'input_3': pn, 'input_4': em}
	for line in infile:
		split=line.split()
		if(split[0]=='____'):
			saved_meals.append(meal)
			meal=dict()
		else:
			meal[split[0]]=split[1]
	return saved_meals


def add_new_meal():
	new_meal={}
	while(True):
		new_meal['input_6']=input("Breakfast, Lunch, or Dinner? ")
		if(new_meal['input_6']=="Breakfast" or new_meal['input_6']=="Lunch" or new_meal['input_6']=="Dinner"):
			break
	new_meal['input_16']=input("Apple Juice, Orange Juice, or Water:")
	if(new_meal['input_6']=="Breakfast"):
		new_meal['input_14']="Bagel with cream cheese"
	else:
		new_meal['input_15']="Piece of fruit (based on seasonal availability)"
		new_meal['input_17']=input("Caesar or Ranch salad dressing:")
		new_meal['input_18']=input("Turkey, Ham, Beef or Custom(May not work):")
		new_meal['input_19']=input("Granola Bar or Pastry Item:")
	new_meal['input_20']=input("Special Requests:")
	write_meal(new_meal)


def write_meal(new_meal):
	infile=open('meals.txt', 'a')
	infile.write("\n")
	for key in new_meal:
		infile.write("\n")
		infile.write(key)
		infile.write(" ")
		infile.write(new_meal[key])
	infile.write("is_submit_3 1\n")
	infile.write("gform_submit 3\n")
	infile.write("state_3 WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0=\n")
	infile.write("____")


#read_meals()
def get_info():
	info={}
	info['fname']=input("First Name:")
	info['lname']=input("Last Name:")
	info['sn']=input("Student Number:")
	info['pn']=input("Phone Number:")
	return info


#add_new_meal()
#r=requests.post(url, data=post_fields)
