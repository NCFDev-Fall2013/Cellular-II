def colourList():
	colours = []
	limbo = open("colours.txt", 'r')
	text = limbo.read().splitlines()
	for line in text:
		strValues = line.split(" ")
		intValues = [int(item) for item in strValues]
		colours.append(tuple(intValues))
	return colours
