import pandas as pd


def pilot_has_required_skills(pilot, mission):

    pilot_skills = [s.strip().lower() for s in pilot["skills"].split(",")]
    required_skill = mission["required_skills"].strip().lower()

    return required_skill in pilot_skills


def pilot_has_required_certs(pilot, mission):

    pilot_certs = [c.strip().lower() for c in pilot["certifications"].split(",")]
    required_certs = [c.strip().lower() for c in mission["required_certs"].split(",")]

    for cert in required_certs:
        if cert not in pilot_certs:
            return False

    return True


def pilot_in_same_location(pilot, mission):

    return pilot["location"].lower() == mission["location"].lower()


def pilot_within_budget(pilot, mission, duration_days=1):

    cost = pilot["daily_rate_inr"] * duration_days

    return cost <= mission["mission_budget_inr"]


def find_best_pilot(mission, pilots):

    available_pilots = pilots[pilots["status"] == "Available"]

    eligible_pilots = []

    for _, pilot in available_pilots.iterrows():

        if not pilot_has_required_skills(pilot, mission):
            continue

        if not pilot_has_required_certs(pilot, mission):
            continue

        if not pilot_in_same_location(pilot, mission):
            continue

        if not pilot_within_budget(pilot, mission):
            continue

        eligible_pilots.append(pilot)

    if len(eligible_pilots) == 0:
        return None

    # choose cheapest pilot
    best = min(eligible_pilots, key=lambda x: x["daily_rate_inr"])

    return best
