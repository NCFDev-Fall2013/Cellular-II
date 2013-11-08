from cells import Cell
import unittest, environment, random, math, weakref, random, globals
from vector import Vector, Point
from functools import partial
from operator import itemgetter, attrgetter


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
        super(Virus,self).__init__(x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0)
        self.bool_moving = False
        self.moving_path = []
        self.ticksLeft = 0
        self.driftSpeed = dS
        self.maxSpeed = dS
        self.curveTendency = cT
        self.lifeSpan = lS
        self.incubation_period = incP
        self.symptom_potency = incP
        self.infection_behavior = infB 
        self.key = k
        self.infection_potency = infP
        self.infector = None

    def keyGen(self):
        self.key = round(random.random(), 2)*100

    def keyGen(self, parent):
        add = round(random.random(), 1)*10
        return parent - (parent%10) + add

    def infect(self, victim):
        print "INFECTING ATTEMPT"
        self.infector = victim
        chance = self.infection_potency #- victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(victim.pos.x, victim.pos.y, victim, self)
            environment.Environment().remove_cell(victim)
            environment.Environment().add_specific_cell_at_location(clone, clone.pos)
        if victim.guessedKey(self.key):
            environment.Environment().kill_cell(self)

    def move_like_virus(self):
        if not self.bool_moving:
            self.ticksLeft = 0
            "Not movin', trying to move... "
            self.bool_moving = True
            print "pos = ", self.pos
            current_pos = self.pos
            ref_pos = Point(0,0)
            self.moving_path_as_string = "x^",self.curveTendency
            print "future path = ", self.moving_path_as_string
            end_of_eY = environment.Environment().height - current_pos.y
            end_of_eX = environment.Environment().width - current_pos.x
            distanceTraveled = 0
            timeLeft = self.lifeSpan
            print "time left = ", timeLeft
            while timeLeft > 0:
                nextPos_ref = Point(ref_pos.x + self.driftSpeed,((ref_pos.x+self.driftSpeed)**self.curveTendency))
                #print "for reference... ", nextPos_ref
                realPos = Point(current_pos.x + nextPos_ref.x, current_pos.y + nextPos_ref.y)
                #print "adding... ", realPos
                self.moving_path.append(realPos)
                ref_pos = nextPos_ref
                timeLeft -= 1
            self.curveTendency = random.randint(1,3)
            multi = random.uniform(-1,1)
            self.driftSpeed = self.maxSpeed * multi/abs(multi)
            #self.driftSpeed = random.uniform(-self.maxSpeed, self.maxSpeed)
            print "curve = ", self.curveTendency
            print "drift = ", self.driftSpeed
            if self.curveTendency > 10:
                self.curveTendency = 3
            elif self.curveTendency <= 0:
                self.curveTendency = 1
        else:
            print "moving now"
            ticksMax = len(self.moving_path)
            #print "path = ", self.moving_path
            print "length of path = ", ticksMax
            print "ticks left = ",  self.ticksLeft
    
            self.pos.x = self.moving_path[self.ticksLeft].x
            self.pos.y = self.moving_path[self.ticksLeft].y
            print "moving to ", self.pos
            self.ticksLeft += 1
            if self.ticksLeft == ticksMax:
                self.bool_moving = False
                self.moving_path = []
                ticksLeft = 0

    def life_and_death(self):
        self.lifeSpan -= 1
        if self.lifeSpan <= 0:
            environment.Environment().kill_cell(self)
    
    def one_tick(self):
        print "virus be tickin"
        self.move_like_virus()
        self.life_and_death()

    def collideWith(self, foe):
        self.infector = foe
        super(Virus, self).collideWith(foe)
        chance = self.infection_potency #- victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(foe.pos.x, foe.pos.y, foe, self)
            if not isinstance(foe, Virus) and not isinstance(foe, InfectedCell):
                if foe in environment.Environment().cell_list:
                    environment.Environment().remove_cell(foe)
                environment.Environment().add_specific_cell_at_location(clone, clone.pos)
        if foe.guessedKey(self.key):
            environment.Environment().kill_cell(self)

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
        
            
    
