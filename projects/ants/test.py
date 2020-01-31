from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
colony = AntColony(None, beehive, ant_types(), layout, (1, 9))
#
# Testing removing a bodyguard doesn't remove contained ant
place = colony.places['tunnel_0_0']
bodyguard = BodyguardAnt()
test_ant = Ant(1)
# add bodyguard first
place.add_insect(bodyguard)
place.add_insect(test_ant)
colony.remove_ant('tunnel_0_0')
print(place.ant is test_ant)