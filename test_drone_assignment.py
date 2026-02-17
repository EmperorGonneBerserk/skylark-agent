from sheets import get_drones, get_missions
from drone_assignment import find_best_drone

drones = get_drones()
missions = get_missions()

mission = missions.iloc[0]  # PRJ001

best_drone = find_best_drone(mission, drones)

if best_drone is not None:
    print("Best Drone Found:")
    print(best_drone["drone_id"], "-", best_drone["model"])
else:
    print("No suitable drone found")
