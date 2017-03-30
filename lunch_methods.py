import os
import datetime

def open_data(dir_loc, file, opentype): #Open the file in the given location and read/write type and return the infile
	directory = ('%s\%s' %(os.getcwd(), dir_loc))	#Generate directory path
	if not os.path.exists(directory):	#Create a new directory for the data if it doesn't already exist
		os.makedirs(directory)
	location=('%s/%s' %(dir_loc, file))		#Generate the location of the specific data file 
	try:
		open(location, 'x')					#Try to create a new file if it doesn't already exist
	except OSError as e:
		pass
	infile=open(location, opentype)			#Open the given file with the given method and return 
	return infile
def clean_dates():
	remove=[]
	today = datetime.datetime.now()
	infile=open_data('data', 'dates.dat', 'r')
	lines=infile.readlines()
	for line in lines:
		print(line)
		split=line.split()
		day=split[1].split('/')
		print(day)
		if(int(day[2])<=today.year):
			if(int(day[0])<=today.month):
				if(int(day[1])<(today.day-1)):
					remove.append(split[1])
	infile.close()
	infile=open('data/dates.dat', 'w')
	print(remove)
	for line in lines:
		date=line.split()[1]
		if date not in remove:
			infile.write(line)

