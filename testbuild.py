
# this is the test build for msync, master program
import opt1
import opt2
import opt3

print("Choose an option for your next step")		#First choice offered
print("1. View Files")
print("2. Search Files")
print("3. Upload Files")
print("4. Exit")

x = 8
while x != 4 : 
	x = int(input("Enter your choice here : "))
	if x == 1 :													#This option opens the list of all the current files in the dictionary
		print("You have chosen to view files")
		opt1.listprint()
		click = input("Press Enter to continue to the main menu")
	elif x == 2 : 												#This option searches the list of all current files from the dictionary
		print("You have chosen to Search for files")
		opt2.searchprint()
		click = input("Press Enter to continue to the main menu")
	elif x == 3 :												#This option should take you to the portal to upload the files
		print("You have chosen to Upload a file")
		opt3.updateprint()
		click = input("Press Enter to continue to the main menu")
	elif x == 4 :												#This option exits your program
		click = input("Press Enter to Exit")
		exit()
	else : 														#For any other invalid input, gives option to either exit or start again
		print('Invalid input')
		y = input('Would you like to see the [O]ptions again or [E]xit ? : ')
		if y.upper() == 'O' :
			x == 1
		elif y.upper() == 'E' :
			exit()
		else :
			print('Invalid input, Exiting the program')			#Second invalid input, exiting the program
			exit()
