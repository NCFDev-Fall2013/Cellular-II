from cells import Cell
import unittest, environment, random, math, weakref, random, globals
from vector import Vector, Point
from functools import partial
from operator import itemgetter, attrgetter

#Virus is a subclass of Cell
class Virus(Cell):
    
    default_emRatio = 2.0
    default_div_energy = 0.5
    default_div_mass = 0.6
    default_color = None
    default_walk_force = 0.001
    default_density = 0.005
    default_mutation_chance = 30
    default_resistance = 0
    Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance]

    def __init__(self, x, y, dS=.0005, cT=2, lS=400, incP=4, infB="on_death_disperse", k=50, infP=.4, mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance]):

        #initialize superclass fields
        super(Virus,self).__init__(x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0)

        #class-scoped tracker for virus movement
        self.bool_moving = False

        #viruses know their future path
        self.moving_path = []
        self.ticksLeft = 0 #used as iterator for movement

        #'speed' of movement - really how quickly the virus moves x coordinates
        self.driftSpeed = dS

        #cap this because driftSpeed is alterable
        self.maxSpeed = dS

        #the exponent of movement along the y axis
        self.curveTendency = cT

        #simple - how long the virus survives
        self.lifeSpan = lS

        #how long it takes for an infected cell's symptoms to show
        self.incubation_period = incP

        #how quickly the symptoms of infection kill the cell
        self.symptom_potency = incP

        #type of infection - a string
        self.infection_behavior = infB

        #viruses have keys - if a cell correctly resists a virus by rolling
        #then the cell will automatically resist viruses with the same key
        self.key = k

        #infection potency is basically the virus' chance of infecting somethign
        self.infection_potency = infP

        #used for infect function
        self.infector = None

    #generates default key for a cell
    def keyGen(self):
        self.key = round(random.random(), 2)*100 #keys are two digit numbers currently

    #generates keys based on inhereted key
    def keyGen(self, parent):
        add = round(random.random(), 1)*10 #random ones place
        return parent - (parent%10) + add #replace ones place from parent with random

    #infection function - obsolete
    #infection is now handled in collideWith overwrite
    """def infect(self, victim):
        print "INFECTING ATTEMPT"
        self.infector = victim 
        chance = self.infection_potency #- victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(victim.pos.x, victim.pos.y, victim, self)
            environment.Environment().remove_cell(victim)
            environment.Environment().add_specific_cell_at_location(clone, clone.pos)
        if victim.guessedKey(self.key):
            environment.Environment().kill_cell(self)"""

    #movement is a little complicated - I'll describe it piece by piece
    #and give a summary at the end
    def move_like_virus(self):
        if not self.bool_moving: #if the cell isn't moving
            self.ticksLeft = 0 #then it's at the beginning - it's made 0 steps
            print "Not movin', trying to move... "
            self.bool_moving = True #get ready to moves
            print "pos = ", self.pos
            current_pos = self.pos #placeholder variable - bad habits from Java
            ref_pos = Point(0,0) #prepare a reference frame based on current location
            self.moving_path_as_string = "x^",self.curveTendency 
            print "future path = ", self.moving_path_as_string
            #end_of_eY = environment.Environment().height - current_pos.y 
            #end_of_eX = environment.Environment().width - current_pos.x
            distanceTraveled = 0 #we haven't gone anywhere yet
            timeLeft = int(self.lifeSpan/3) #viruses choose three paths in their life
            print "time left = ", timeLeft
            while timeLeft > 0: #we begin adding positions in the virus' trajectory
                #nextPos_ref is the projected position based on a null reference frame
                nextPos_ref = Point(ref_pos.x + self.driftSpeed,((ref_pos.x+self.driftSpeed)**self.curveTendency))
                #print "for reference... ", nextPos_ref
                #realPos adds the reference frame position to the actual position
                realPos = Point(current_pos.x + nextPos_ref.x, current_pos.y + nextPos_ref.y)
                #print "adding... ", realPos
                self.moving_path.append(realPos)
                #the reference doesn't reset, but builds upon itself
                ref_pos = nextPos_ref
                #decrease steps left
                timeLeft -= 1
            #now that movement has been predicted, we prepare for next movement    
            #change curve which is being followed
            self.curveTendency = random.randint(1,3)
            multi = random.uniform(-1,1)
            #change direction possibly
            self.driftSpeed = self.maxSpeed * multi/abs(multi)
            #self.driftSpeed = random.uniform(-self.maxSpeed, self.maxSpeed)
            print "curve = ", self.curveTendency
            print "drift = ", self.driftSpeed
            #these should ever be used, but just in case
            if self.curveTendency > 10:
                self.curveTendency = 3
            elif self.curveTendency <= 0:
                self.curveTendency = 1
        else: #we're moving!
            print "moving now"
            ticksMax = len(self.moving_path) #how many steps are to be taken?
            #print "path = ", self.moving_path
            print "length of path = ", ticksMax
            print "ticks left = ",  self.ticksLeft

            #change x and y
            self.pos.x = self.moving_path[self.ticksLeft].x
            self.pos.y = self.moving_path[self.ticksLeft].y
            print "moving to ", self.pos

            #remeber ticksLeft? Here it's used
            self.ticksLeft += 1
            if self.ticksLeft == ticksMax: #when we've reached the end
                self.bool_moving = False #stop
                self.moving_path = [] #empty the path
                ticksLeft = 0 #reset ticksLeft

    #viruses have a simpler existence than cells
    def life_and_death(self):
        self.lifeSpan -= 1 #they just die after a time
        if self.lifeSpan <= 0:
            environment.Environment().kill_cell(self)

    #overwrite one_tick
    def one_tick(self):
        print "virus be tickin"
        self.move_like_virus()
        self.life_and_death()

    #overwrite collision - here infection happens
    def collideWith(self, foe):
        self.infector = foe 
        super(Virus, self).collideWith(foe) #use Cell collision - i.e. actually collide
        chance = self.infection_potency #- victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(foe.pos.x, foe.pos.y, foe, self) #make a clone
            if not isinstance(foe, Virus) and not isinstance(foe, InfectedCell): #don't infect viruses or already infected cells
                if foe in environment.Environment().cell_list: #some issues occured with the Cell_List - this fixes it
                    environment.Environment().remove_cell(foe) #remove old cell
                environment.Environment().add_specific_cell_at_location(clone, clone.pos) #add the infected
        if foe.guessedKey(self.key): #if the foe correctly guessed the virus' key
            environment.Environment().kill_cell(self) #kill that virus!
        #GUESSKEY NEEDS TO BE MOVED TO ABOVE THE INFECTION
            
class InfectedCell(Cell):

    default_emRatio = 2.0
    default_div_energy = 0.5
    default_div_mass = 0.6
    default_color = None
    default_walk_force = 0.001
    default_density = 0.005
    default_mutation_chance = 30
    default_resistance = 0
    
    def __init__(self, x, y, cell, virus, incP=20, infB="on_death_disperse", k=50, infP=.2, mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance]):
        super(InfectedCell,self).__init__(x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0)
        self.pastSelf = cell
        self.timeTilSymptoms = incP #should be a natural number
        self.iTimeTilSymptoms = incP
        self.timeToDie = incP*.01
        self.keyForChildren = k
        self.typeOfInfection = infB
        self.parent = cell
        self.killer = virus
        self.bool_showingSymptoms = False
        self.dispersionCount = 2
    
    def one_tick(self):
        super(InfectedCell, self).one_tick()
        self.timeTilSymptoms -= 1
        if self.timeTilSymptoms <= 0:
            self.bool_showingSymptoms = True

    def life_and_death(self):
        if not self.bool_showingSymptoms:
            super(InfectedCell, self).life_and_death()
        elif self.typeOfInfection == "on_death_disperse":
            #self.dispersionCount += self.timeTilSymptoms % 10
            if self.energy > self.timeToDie:
                self.energy -= self.timeToDie
            else:
                self.mass -= self.timeToDie
                if self.mass <= 0.1:
                    environment.Environment().add_viruses_at_loc(self.dispersionCount,self.killer.pos)
                    environment.Environment().kill_cell(self)
                    passer = self.keyForChildren - (self.keyForChildren % 10)
                    self.killer.keyGen(passer)                          
        
            
    
