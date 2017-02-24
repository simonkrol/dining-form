import requests
import os



url = 'http://dining.carleton.ca/locations/fresh-food-company/' # Set destination URL here
def read_meals():
	try:
		open('meals.txt', 'x')
	except OSError as e:
		pass
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
			meal[split[0]]=' '.join(split[1:len(split)])
	return saved_meals


def add_new_meal():
	new_meal={}
	while(True):
		new_meal['input_6']=input("Breakfast, Lunch, or Dinner? ")
		if(new_meal['input_6']=="Breakfast" or new_meal['input_6']=="Lunch" or new_meal['input_6']=="Dinner"):
			break
		cls()
	new_meal['input_16']=input("Apple Juice, Orange Juice, or Water:")
	if(new_meal['input_6']=="Breakfast"):
		new_meal['input_14']="Bagel with cream cheese"
	else:
		new_meal['input_15']="Piece of fruit(based on seasonal availability)"
		new_meal['input_17']=input("Caesar or Ranch salad dressing:")
		new_meal['input_18']=input("Turkey, Ham, Beef or Custom(May not work):")
		new_meal['input_19']=input("Granola Bar or Pastry Item:")
	new_meal['input_20']=input("Special Requests:")
	cls()
	write_meal(new_meal)


def write_meal(new_meal):
	try:
		open('meals.txt', 'x')
	except OSError as e:
		pass
	infile=open('meals.txt', 'a')
	for key in new_meal:
		infile.write("\n")
		infile.write(key)
		infile.write(" ")
		infile.write(new_meal[key])
	infile.write("\nis_submit_3 1\n")
	infile.write("gform_submit 3\n")
	infile.write("state_3 WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0=\n")
	infile.write("____")

def print_meals(meals):
	for meal in meals:
		print("Meal #", meals.index(meal), "(", meal['input_6'], "):")
		for key in meal:
			if(key[:2]=="in" and key != "input_6"):
				print(meal[key])
		print("\n")



#read_meals()
def get_info():
	info={}
	info['input_1.3']=input("First Name:")
	info['input_1.6']=input("Last Name:")
	info['input_2']=input("Student Number:")
	info['input_3']=input("Phone Number:")
	info['input_4']=input("Email adress:")
	cls()
	return info


def main():
	cls()
	get_info()
	s_meals=read_meals()
	while(True):
		choice=int(input("Press 1 to add a meal, 2 to print current meals, or 3 to order a meal:"))
		cls()
		if(choice==1):
			add_new_meal()
			s_meals=read_meals()
		elif(choice==2):
			print_meals(s_meals)
		elif(choice==3):
			pass#order_meal()
		else:
			print("Invalid option, please try again")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


main()
#r=requests.post(url, data=post_fields)



