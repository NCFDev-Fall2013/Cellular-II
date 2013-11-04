from cells import Cell
import unittest, environment, random, math, weakref, random, globals
from vector import Vector, Point
from functools import partial
from operator import itemgetter, attrgetter


class Virus(Cell):
    
    bool_moving = False
    moving_path = []

    default_emRatio = 2.0
    default_div_energy = 0.5
    default_div_mass = 0.6
    default_color = None
    default_walk_force = 0.001
    default_density = 0.005
    default_mutation_chance = 30
    default_resistance = 0

    def __init__(self, x, y, dS, cT, lS, incP, infB, k, infP, mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance]):
        super(Virus,self).__init__(x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance])
        self.driftSpeed = dS
        self.curveTendency = cT
        self.lifeSpan = lS
        self.incubation_period = incP
        self.symptom_potency = incP
        self.infection_behavior = infB 
        self.key = k
        self.infection_potency = infP
        self.environment = e

    def keyGen(self):
        key = round(random.random(), 2)*100

    def keyGen(self, parent):
        add = round(random.random(), 1)*10
        return parent - (parent%10) + add

    def infect(self, victim):
        chance = infection_potency - victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(victim, incubation_period, symptom_potency, key)
            environment.remove_cell(victim)
            environment.add_specific_cell_at(clone, victim.pos)
        if victim.guessedKey(key):
            environment.kill(self)

    def move_like_virus(self):
        if not bool_moving:
            bool_moving = True
            current_pos = self.pos
            moving_path_as_string = "x^",curveTendency
            end_of_eY = environment.height - current_pos.y
            end_of_eX = environment.width - current_pos.x
            distanceTraveled = 0
            timeLeft = math.abs(round(curveTendency,0) + 1)
            while timeLeft > 0:
                nextPos = Point(current_pos.x + driftSpeed, (driftSpeed/math.abs(driftSpeed))*(current_pos.x**curveTendency))
                moving_path.append(nextPos)
                current_pos = nextPos
                timeLeft -= 1
            curveTendency *= random.randomInteger()
            if curveTendency > 10:
                curveTendency = 10
            elif curveTendency <= 0:
                curveTendency = 1
        else:
            ticksMax = move_path.length
            ticksLeft = 0
            self.pos.x = move_path[ticksLeft].x
            self.ps.y = move_path[ticksLeft].y
            ticksLeft += 1
            if licksLeft == ticksMax:
                bool_moving = False
                moving_path = []

    def one_tick(self):
        self.move_like_virus()
        self.life_and_destruction()

class InfectedCell(Cell):

    default_emRatio = 2.0
    default_div_energy = 0.5
    default_div_mass = 0.6
    default_color = None
    default_walk_force = 0.001
    default_density = 0.005
    default_mutation_chance = 30
    default_resistance = 0
    bool_showingSymptoms = False
    dispersionCount = 0
    
    def __init__(self, x, y, cell,iPeriod,iTime, symPot, parentKey, iBeh, virus, mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance]):
        super(InfectedCell,self).__init__(x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[default_emRatio, default_div_energy, default_div_mass, default_color, default_walk_force, default_density , default_mutation_chance])
        self.pastSelf = cell
        self.timeTilSymptoms = iPeriod #should be a natural number
        self.iTimeTilSymptoms = iTime
        self.timeToDie = symPot
        self.keyForChildren = parentKey
        self.typeOfInfection = iBeh
        self.parent = cell
        self.killer = virus
    
    def one_tick(self):
        super.one_tick()
        timeTilSymptoms -= 1
        if timeTilSymptoms <= 0:
            bool_showingSymptoms = True

    def life_and_death(self):
        if not bool_showingSymptoms:
            Cell.life_and_death()
        elif typeOfInfection == "on_death_disperse":
            dispersionCount += timeTillSymptoms % 10
            if self.energy > timeToDie:
                self.energy -= timeToDie
            else:
                self.mass -= timeToDie
                if self.mass <= 0.1:
                    environment.Environment().kill_cell(self)
                    passer = keyForChildren - (keyForChildren % 10)
                    killer.keyGen(passer)
                    environment.Environment().add_cells(dispersionCount,killer,self.pos)
                    
                
            
            

    
