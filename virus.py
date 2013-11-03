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

    def keyGen(self):
        key = round(random.random(), 2)*100

    def keyGen(self, parent):
        add = round(random.random(), 1)*10
        return parent - (parent%10) + add

    def infect(self, victim):
        chance = infection_potency - victim.resistance
        if random.random() <= chance:
            clone = InfectedCell(victim, incubation_period, symptom_potency, key)
            e.remove_cell(victim)
            e.add_specific_cell_at(clone, victim.pos)
        if victim.guessedKey(key):
            e.kill(self)


class InfectedCell(Cell, cell, iPeriod, symPot, parentKey):
    
