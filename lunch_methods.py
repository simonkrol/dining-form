import os

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