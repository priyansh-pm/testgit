#this will be changes that i should find out on the master branch
#this is testbuild for msync, Option 2
def searchprint() :
	y = input('Name of the file you want to search for : ')
	with open("testfilelist.txt", "r") as f:
		searchlines = f.readlines()
	for i, line in enumerate(searchlines):
		if y in line: 
			for l in searchlines[i:i+1]: 
				print(l),
			
# PLS SEE : IMPLEMENT DOWNLOAD AFTER FILE SELECTION #			