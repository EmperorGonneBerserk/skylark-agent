from sheets import get_pilots, get_drones, get_missions, update_pilot_status, update_drone_status
from assignment import find_best_pilot
from drone_assignment import find_best_drone
from conflict_detection import detect_conflicts


def assign_mission(project_id):

    pilots = get_pilots()
    drones = get_drones()
    missions = get_missions()

    mission = missions[missions["project_id"] == project_id]

    if mission.empty:
        return f"Mission {project_id} not found"

    mission = mission.iloc[0]

    pilot = find_best_pilot(mission, pilots)

    if pilot is None:
        return "No suitable pilot available"

    drone = find_best_drone(mission, drones)

    if drone is None:
        return "No suitable drone available"

    conflicts = detect_conflicts(pilot, drone, mission)

    if len(conflicts) > 0:

        conflict_text = "\n".join(conflicts)

        return f"Conflicts detected:\n{conflict_text}"

    # Update sheets
    update_pilot_status(pilot["pilot_id"], "Assigned")
    update_drone_status(drone["drone_id"], "Assigned")

    return f"""
Mission Assigned Successfully

Pilot: {pilot['name']}
Drone: {drone['drone_id']} ({drone['model']})
Location: {mission['location']}
"""


def show_available_pilots():

    pilots = get_pilots()

    available = pilots[pilots["status"] == "Available"]

    if available.empty:
        return "No pilots available"

    result = "Available Pilots:\n"

    for _, pilot in available.iterrows():
        result += f"{pilot['pilot_id']} - {pilot['name']} ({pilot['location']})\n"

    return result


def show_available_drones():

    drones = get_drones()

    available = drones[drones["status"] == "Available"]

    if available.empty:
        return "No drones available"

    result = "Available Drones:\n"

    for _, drone in available.iterrows():
        result += f"{drone['drone_id']} - {drone['model']} ({drone['location']})\n"

    return result


def urgent_reassignment(project_id):

    return assign_mission(project_id)


def handle_query(user_input):

    user_input = user_input.lower()

    if "assign" in user_input:

        project_id = user_input.upper().split()[-1]

        return assign_mission(project_id)

    elif "available pilots" in user_input:

        return show_available_pilots()

    elif "available drones" in user_input:

        return show_available_drones()

    elif "urgent" in user_input:

        project_id = user_input.upper().split()[-1]

        return urgent_reassignment(project_id)

    else:

        return "I can help assign pilots, show availability, and manage missions."
