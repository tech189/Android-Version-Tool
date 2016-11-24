#a dictionary containing all info about each version
#data taken from https://en.wikipedia.org/wiki/Android_version_history
version = {
		"1.0": ["Alpha", "September 23, 2008", [], "1"],
		"1.1": ["Beta", "February 9, 2009", [], "2"],
		"1.5": ["Cupcake", "April 27, 2009", [], "3"],
		"1.6": ["Donut", "September 15, 2009", [], "4"],
		"2.0": ["Eclair", "October 26, 2009", ["2.0.1", "2.1"], "5"],
		"2.0.1": ["Eclair", "December 3, 2009", [], "6"],
		"2.1": ["Eclair", "January 12, 2010", [], "7"],
		"2.2": ["Froyo", "May 20, 2010", ["2.2.1", "2.2.2", "2.2.3"], "8"],
		"2.2.1": ["Froyo", "January 18, 2011", [], "8"],
		"2.2.2": ["Froyo", "January 22, 2011", [], "8"],
		"2.2.3": ["Froyo", "November 21, 2011", [], "8"],
		"2.3": ["Gingerbread", "December 6, 2010", ["2.3.1", "2.3.2", "2.3.3", "2.3.4", "2.3.5", "2.3.6", "2.3.7"], "9"],
		"2.3.1": ["Gingerbread", "December 2010", [], "9"],
		"2.3.2": ["Gingerbread", "February 9, 2011", [], "10"],
		"2.3.3": ["Gingerbread", "February 9, 2011", [], "10"],
		"2.3.4": ["Gingerbread", "April 28, 2011", [], "10"],
		"2.3.5": ["Gingerbread", "July 25, 2011", [], "10"],
		"2.3.6": ["Gingerbread", "September 2, 2011", [], "10"],
		"2.3.7": ["Gingerbread", "September 21, 2011", [], "10"],
		"3.0": ["Honeycomb", "February 22, 2011", ["3.1", "3.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.2.6"], "11"],
		"3.1": ["Honeycomb", "May 10, 2011", [], "12"],
		"3.2": ["Honeycomb", "July 15, 2011", ["3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.2.6"], "13"],
		"3.2.1": ["Honeycomb", "September 20, 2011", [], "13"],
		"3.2.2": ["Honeycomb", "August 30, 2011", [], "13"],
		"3.2.3": ["Honeycomb", "unknown", [], "13"],
		"3.2.4": ["Honeycomb", "December 2011", [], "13"],
		"3.2.5": ["Honeycomb", "January 2012", [], "13"],
		"3.2.6": ["Honeycomb", "February 2012", [], "13"],
		"4.0": ["Ice Cream Sandwich", "October 18, 2011", ["4.0.1", "4.0.2", "4.0.3", "4.0.4"], "14"],
		"4.0.1": ["Ice Cream Sandwich", "October 21, 2011", [], "14"],
		"4.0.2": ["Ice Cream Sandwich", "November 28, 2011", [], "14"],
		"4.0.3": ["Ice Cream Sandwich", "December 16, 2011", [], "15"],
		"4.0.4": ["Ice Cream Sandwich", "March 29, 2012", [], "15"],
		"4.1": ["Jelly Bean", "July 9, 2012", ["4.1.1", "4.1.2", "4.2", "4.2.1", "4.2.2", "4.3", "4.3.1"], "16"],
		"4.1.1": ["Jelly Bean", "July 11, 2012", [], "16"],
		"4.1.2": ["Jelly Bean", "October 9, 2012", [], "16"],
		"4.2": ["Jelly Bean", "November 13, 2012", [], "17"],
		"4.2.1": ["Jelly Bean", "November 27, 2012", [], "17"],
		"4.2.2": ["Jelly Bean", "February 11, 2013", [], "17"],
		"4.3": ["Jelly Bean", "July 24, 2013", [], "18"],
		"4.3.1": ["Jelly Bean", "October 3, 2013", [], "18"],
		"4.4": ["KitKat", "October 31, 2013", ["4.4.1", "4.4.2", "4.4.3", "4.4.4"], "19"],
		"4.4.1": ["KitKat", "December 5, 2013", [], "19"],
		"4.4.2": ["KitKat", "December 9, 2013", [], "19"],
		"4.4.3": ["KitKat", "June 2, 2014", [], "19"],
		"4.4.4": ["KitKat", "June 19, 2014", [], "19"],
		"5.0": ["Lollipop", "November 12, 2014", ["5.0.1", "5.0.2", "5.1", "5.1.1"], "21-22"],
		"5.0.1": ["Lollipop", "December 2, 2014", [], "21"],
		"5.0.2": ["Lollipop", "December 19, 2014", [], "21"],
		"5.1": ["Lollipop", "March 9, 2015", ["5.1.1"], "22"],
		"5.1.1": ["Lollipop", ],
		"6.0": ["Marshmallow", "October 5, 2015", ["6.0.1"], "23"],
		"6.0.1": ["Marshmallow", "December 7, 2015", [], "23"],
		"7.0": ["Nougat", "August 22, 2016", ["7.1", "7.1.1"], "24-25"],
		"7.1": ["Nougat", "October 4, 2016", ["7.1.1"], "25"],
		"7.1.1": ["Nougat", "not yet released", [], "25"]
		}

#initialising the input variables
the_input = ""
another_input = ""

def check_input():
	#this function checks what the user wants and whether it's valid

	#ask the user what they want
	the_input = input("\nWhat would you like to know? Type:\n\ncode name \t to look up the code name of an Android version\nrelease date \t to find when an Android version was released\nminor release \t to look up the minor releases of an Android version\napi level \t to look up the API level for an Android version\n(control + c will exit the program at any time)\n\n")

	#decide which function to call based on what the user typed in
	if the_input == "code name":
		get_codename()
	elif the_input == "release date":
		get_releasedate()
	elif the_input == "minor release":
		get_minorrelease()
	elif the_input == "api level":
		get_apilevel()
	#reject non valid inputs and prompt user to try again
	else:
		print("\n------------------------------------\nNot a valid input, please try again.\n------------------------------------")
		check_input()

def another_go():
	#this function deals with if the user wants another go

	the_input = input("\nDo you want to look something else up? (yes/no)\n\n")

	if the_input == "yes":
		the_input = input("\nWhat would you like to know? Type:\ncode name - to look up the code name of an Android version\nrelease date - to find when an Android version was released\nminor release - to look up the minor releases of an Android version\napi level - to look up the API level for an Android version\n(control + c will exit the program at any time)\n\n")

		#decide which function to call based on what the user typed in
		if the_input == "code name":
			get_codename()
		elif the_input == "release date":
			get_releasedate()
		elif the_input == "minor release":
			get_minorrelease()
		elif the_input == "api level":
			get_apilevel()

		#reject non valid inputs and prompt user to try again
		else:
			print("\n------------------------------------\nNot a valid input, please try again.\n------------------------------------")
			check_input()
	else:
		print("\nExiting...")
		import sys
		sys.exit()

def get_codename():
	#gets the code name of the version

	#ask user to type in a version number
	the_input = input("\nEnter an Android version number: ")

	#check for valid input and prompt user to try again
	if not the_input in version:
		print("\n------------------------------------\nNot a valid version number.\n------------------------------------")
		get_codename()
	else:
		#print out the code name by referencing the dictionary
		print("\nThe code name for version number " + str(the_input) + " is " + version[the_input][0] + ".")
	another_go()

def get_releasedate():
	#gets the release date of a version

	#ask user to type in a version
	the_input = input("\nEnter an Android version number: ")

	#check for valid input and prompt user to try again
	if not the_input in version:
		print("\n------------------------------------\nNot a valid version number.\n------------------------------------")
		get_releasedate()
	else:
		#print out release date by referencing the dictionary
		print("\nThe release date for version number " + str(the_input) + " was " + version[the_input][1] + ".")
	another_go()

def get_minorrelease():
	#gets the number of minor releases and can print them out

	#ask user to type in a version
	the_input = input("\nEnter an Android version number: ")

	#check for valid input and prompt user to try again
	if not the_input in version:
		print("\n------------------------------------\nNot a valid version number.\n------------------------------------")
		get_minorrelease()
	else:
		#choose what to print
		if len(version[the_input][2]) == 0:
			print("\nFor version " + str(the_input) + " there were no minor releases.")
		else:
			#print out number of minor releases by referencing the dictionary
			print("\nFor version " + str(the_input) + " there were " + str(len(version[the_input][2])) + " minor release(s).")

		#ask if user wants more info
		another_input = input("\nDo you want to know the minor release version numbers? (yes/no): ")
		print("")
		if another_input == "yes":
			for item in version[the_input][2]:
				print(item)
		else:
			print("\nExiting...")
	another_go()

def get_apilevel():
	#gets the api level of a version

	#asks user to type in a version
	the_input = input("\nEnter an Android version number: ")

	#check for valid input and prompt user to try again
	if not the_input in version:
		print("\n------------------------------------\nNot a valid version number.\n------------------------------------")
		get_apilevel()
	else:
		#print out api level by referencing the dictionary
		print("\nFor version " + str(the_input) + ", the API level is " + str(version[the_input][3]) + ".")
	another_go()

check_input()
