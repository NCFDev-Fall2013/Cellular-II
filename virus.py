class Virus(Cell):
    driftSpeed =
    curveTendency =
    lifeSpan =
    incubation_period =
    symptom_potency =
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
                nextPos = Point(current_pos.x + speed, (speed/math.abs(speed))*(speedcurrent_pos.x**curveTendency))
                moving_path.append(nextPos)
                current_pos = nextPos
                timeLeft--
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

class InfectedCell(Cell, cell, iPeriod, symPot, parentKey):
    
