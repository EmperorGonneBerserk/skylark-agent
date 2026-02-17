from sheets import get_pilots, get_drones, get_missions
from assignment import find_best_pilot
from drone_assignment import find_best_drone
from conflict_detection import detect_conflicts

pilots = get_pilots()
drones = get_drones()
missions = get_missions()

mission = missions.iloc[0]

pilot = find_best_pilot(mission, pilots)
drone = find_best_drone(mission, drones)

conflicts = detect_conflicts(pilot, drone, mission)

if len(conflicts) == 0:
    print("No conflicts detected")
else:
    print("Conflicts:")
    for c in conflicts:
        print("-", c)
