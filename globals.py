def colorList():
    colors = []
    limbo = open("colors.txt", 'r')
    text = limbo.read().splitlines()
    for line in text:
        strValues = line.split(" ")
        intValues = [int(item) for item in strValues]
        colors.append(tuple(intValues))
    return colors
