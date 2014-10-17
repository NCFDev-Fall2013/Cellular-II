NCF Software Development
Fall Semester
Cellular Simulator 

System Requirements:
	Linux OS
	Python 2.7
	Pygame 1.9.1

Installing and Running:
	Make sure you have Python 2.7 and Pygame 1.9.1.
	Navigate to the Github repository and download to a local repository
		URL: 	https://github.com/NCFDev-Fall2013/Cellular-II.git
	Using the terminal, navigate to the local repository 
	Make any changes to config.ini if you wish to change the default template for cells. 
	In the terminal run main.py through python. 
		python main.py
	On the same line, enter arguments which will determine the initial conditions for the program
	The first and second arguments are necessary, and they determine the starting amounts of Food and Cells respectively.
	The third argument is optional and determines the starting amount of viruses. 

	While the program is running, users may insert actors into the environment using the corresponding buttons in the integrated User Interface, or else the user may use the mouse. The left mouse button inserts food, the right mouse button inserts cells, and the middle mouse button inserts viruses. 

About the Actors:

Food-
	Food appears randomly in the environment. When cells ingest food, they obtain mass and energy. 

Cells-
	Cells are the main actors in the environment. They wander aimlessly for a time, but when a piece of food enters their sight, they pursue it singlemindedly. As they eat, they grow, and as they grow, they move more slowly. Once a cell has reached a certain threshold of energy, they are able to divide into two smaller cells. When dividing, there is a chance of mutation, which will change the default characteristics of the cells. Cells also collide with one another. 

Viruses-
	Viruses are beings of wanton cellular destruction. They float through the environment mindlessly, and when they collide with a cell, the cell is infected, dies, and then releases more viruses into the environment. 
	(Note - when many viruses appear in the environment at one time, the program tends to run slowly)



