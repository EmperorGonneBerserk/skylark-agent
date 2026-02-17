from sheets import get_pilots, get_missions
from assignment import find_best_pilot

pilots = get_pilots()
missions = get_missions()

mission = missions.iloc[0]  # PRJ001

best_pilot = find_best_pilot(mission, pilots)

if best_pilot is not None:
    print("Best Pilot Found:")
    print(best_pilot["name"])
else:
    print("No suitable pilot found")
