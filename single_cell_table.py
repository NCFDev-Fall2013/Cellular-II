def check_cell(n,filename):
	"""When given a particular cell and a filename, pulls from the filename and
	outputs a new table with just stats for just that cell."""
	# Constructs the new filename
	werd = "Single_Cell_"+str(n)+" "+filename
	
	# Opens the grand table, assigns it to f1
	f0 = open(filename,"r")
	f1 = f0.read()
	f0.close()
	f1 = f1.split("\n") # Formats the table
	
	# Opens the new file and gives it a header
	fN = open(werd,"w")
	fN.write("\nt\tx_pos	y_pos	x_vel	y_vel	x_dest	y_dest	radius	energy	task\n")
	
	# Adds each line of the grand table with the right cell to the new file
	counter = 0
	ln = len(str(n))+5
	for line in f1:
		if line.startswith("Cell_"+str(n)+"\t"):
			fN.write(str(counter)+line[ln:]+"\n")
			counter +=1
	fN.close()

def main():
	"""Creates a table specifically for one cell.""" 
	# Asks for a filename, then continues to offer to make tables for cells
	filename = raw_input("For which document (include .txt)? ")
	while True:
		cell = input("Which cell would you like to make a table of? ")
        	check_cell(cell,filename)
main()
