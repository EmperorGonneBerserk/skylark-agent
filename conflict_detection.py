def check_pilot_availability(pilot):

    if pilot["status"].lower() != "available":
        return f"Pilot {pilot['name']} is not available"

    return None


def check_drone_availability(drone):

    if drone["status"].lower() != "available":
        return f"Drone {drone['drone_id']} is not available"

    return None


def check_drone_maintenance(drone):

    if drone["status"].lower() == "maintenance":
        return f"Drone {drone['drone_id']} is in maintenance"

    return None


def check_weather_risk(drone, mission):

    weather = mission["weather_forecast"].lower()

    resistance = drone["weather_resistance"].lower()

    if weather == "rainy" and "ip43" not in resistance:

        return f"Drone {drone['drone_id']} not safe for rainy weather"

    return None


def check_budget(pilot, mission, duration_days=1):

    cost = pilot["daily_rate_inr"] * duration_days

    if cost > mission["mission_budget_inr"]:

        return f"Pilot cost exceeds mission budget"

    return None


def check_location_match(pilot, drone, mission):

    if pilot["location"].lower() != mission["location"].lower():

        return "Pilot not in mission location"

    if drone["location"].lower() != mission["location"].lower():

        return "Drone not in mission location"

    return None


def detect_conflicts(pilot, drone, mission):

    conflicts = []

    checks = [
        check_pilot_availability(pilot),
        check_drone_availability(drone),
        check_drone_maintenance(drone),
        check_weather_risk(drone, mission),
        check_budget(pilot, mission),
        check_location_match(pilot, drone, mission),
    ]

    for check in checks:

        if check is not None:
            conflicts.append(check)

    return conflicts
