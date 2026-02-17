def drone_is_available(drone):

    return drone["status"].lower() == "available"


def drone_in_same_location(drone, mission):

    return drone["location"].lower() == mission["location"].lower()


def drone_has_required_capability(drone, mission):

    capability_map = {
        "mapping": ["lidar", "rgb"],
        "inspection": ["rgb"],
        "thermal": ["thermal"],
        "survey": ["lidar", "rgb"]
    }

    drone_caps = [c.strip().lower() for c in drone["capabilities"].split(",")]

    required_skill = mission["required_skills"].strip().lower()

    if required_skill not in capability_map:
        return False

    valid_caps = capability_map[required_skill]

    for cap in drone_caps:
        if cap in valid_caps:
            return True

    return False


def drone_weather_compatible(drone, mission):

    weather = mission["weather_forecast"].lower()

    resistance = drone["weather_resistance"].lower()

    if weather == "rainy":

        return "ip43" in resistance

    return True


def drone_not_in_maintenance(drone):

    return drone["status"].lower() != "maintenance"


def find_best_drone(mission, drones):

    eligible_drones = []

    for _, drone in drones.iterrows():

        if not drone_is_available(drone):
            continue

        if not drone_not_in_maintenance(drone):
            continue

        if not drone_in_same_location(drone, mission):
            continue

        if not drone_has_required_capability(drone, mission):
            continue

        if not drone_weather_compatible(drone, mission):
            continue

        eligible_drones.append(drone)

    if len(eligible_drones) == 0:
        return None

    return eligible_drones[0]
