from Animal import *
from Plant import *

TYPES = {
    'Wolf' : Wolf,
    'Sheep' : Sheep,
    'Fox' : Fox,
    'Turtle' : Turtle,
    'Antelope' : Antelope,
    'CyberSheep' : CyberSheep,
    'Human' : Human,

    'Grass' : Grass,
    'SowThistle' : SowThistle,
    'Guarana' : Guarana,
    'Belladonna' : Belladonna,
    'SosnowskysHogweed' : SosnowskysHogweed
}

class GameState:
    def __init__(self):
        pass

    def save(self, world):
        file = open('save.txt', 'w')

        for i in world.Organisms:
            file.write(type(i).__name__)
            file.write(" ")
            file.write(str(i.x) + " " + str(i.y) + " " + str(i.age))
            if issubclass(type(i), Animal):
                file.write(" " + str(i.strength) + " " + str(i.prev_x) + " " + str(i.prev_y) + " " + str(i.breeding_delay))
                if type(i) == Human:
                    file.write(" " + str(i.abilityDuration) + " " + str(i.abilityCount))
            file.write("\n")

        file.close()

    def load(self, world):
        file = open('save.txt')

        world.Organisms.clear()

        for i in file:
            organism = i.split()
            org_type = TYPES[organism[0]]
            o = org_type(int(organism[1]), int(organism[2]), world)
            o.age = int(organism[3])
            if issubclass(org_type, Animal):
                o.strength = int(organism[4])
                o.prev_x = int(organism[5])
                o.prev_y = int(organism[6])
                o.breeding_delay = int(organism[7])

                if(org_type == Human):
                    if organism[8] == 'True':
                        o.abilityDuration = True
                    else:
                        o.abilityDuration = False
                    
                    o.abilityCount = int(organism[9])