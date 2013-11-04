class Virus(Cell):
    driftSpeed =
    curveTendency =
    lifeSpan =
    incubation_period =
    symptom_potency =
    infection_behavior = 
    color =
    key =
    infection_potency =
    environment = 
    bool_moving = FALSE
    moving_path = []

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

    def move_like_virus(self)
        if !bool_moving:
            bool_moving = TRUE
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
                timeLeft--
            curveTendency *= random.randomInteger()
            if curveTendency > 10:
                curveTendency = 10
            elif curveTendency <= 0:
                curveTendency = 1
        else:
            ticksMax = move_path.length
            ticksLeft = 0
            while ticksLeft <= ticksMax:
                self.pos.x = move_path[ticksLeft].x
                self.ps.y = move_path[ticksLeft].y
                ticksLeft++
            bool_moving = FALSE    

    def one_tick(self):
        self.move_like_virus()
        self.life_and_destruction()

class InfectedCell(Cell, cell, virus, iPeriod, symPot, iBeh, parentKey):
    pastSelf = cell
    timeTilSymptoms = iPeriod #should be a natural number
    iTimeTilSymptoms
    timeToDie = symPot
    keyForChildren = parentKey
    typeOfInfection = iBeh
    bool_showingSymptoms = FALSE
    dispersionCount = 0
    parent = cell
    killer = virus
    
    def one_tick(self):
        Cell.one_tick()
        timeTilSymptoms--
        if timeTilSymptoms <= 0:
            bool_showingSymptoms = TRUE

    def life_and_death(self):
        if !bool_showingSymptoms:
            Cell.life_and_death()
        elif typeOfInfection = "on_death_disperse":
            dispersionCount += timeTillSymptoms % 10
            if self.energy > timeToDie:
                self.energy -= timeToDie
            else:
                self.mass -= timeToDie
                if: self.mass <= 0.1:
                    environment.Environment().kill_cell(self)
                    passer = keyForChildren - (keyForChildren % 10)
                    killer.keyGen(passer)
                    environment.Environment().add_cells(dispersionCount,killer,self.pos)
                    
                
            
            

    
