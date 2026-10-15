
"""Campus shuttle timetable and fleet tracker."""

import json
import secrets
from pathlib import Path

routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}
MIN_CAPACITY = 10


def add_trip_log(route_id, passenger_count, logs=None):
    """Record a trip and return its log entries."""
    if route_id not in routes:
        raise KeyError(f"Unknown route: {route_id}")
    if not isinstance(passenger_count, int) or passenger_count < 0:
        raise ValueError("Passenger count must be a non-negative integer.")

    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(f"{route_id}: carried {passenger_count} passengers")
    return logs


def remove_route(route_id):
    """Remove a route if it exists."""
    if route_id not in routes:
        raise KeyError(f"Unknown route: {route_id}")
    del routes[route_id]


def average_load(route_id):
    """Calculate the average passenger count for a route."""
    if route_id not in routes:
        raise KeyError(f"Unknown route: {route_id}")

    trips = routes[route_id]["trips"]
    return sum(trips) / len(trips) if trips else 0.0


def underused_routes():
    """Return routes whose average load is below minimum capacity."""
    flagged = []
    for route_id in routes:
        if average_load(route_id) < MIN_CAPACITY:
            flagged.append(route_id)
    return flagged


def assign_driver():
    """Select a driver using a cryptographically secure choice."""
    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save fleet data to JSON and load it back safely."""
    path = Path(file)
    path.write_text(json.dumps(routes, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    """Run a sample shuttle-tracker session."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)

    print("Driver for R1:", assign_driver())
    print("Underused routes:", underused_routes())
    print("R1 average:", average_load("R1"))

    sync_fleet_data()

    choice = input("Route to look up (Enter for R2): ").strip() or "R2"
    if choice in routes:
        print("Trips on", choice, ":", routes[choice]["trips"])
    else:
        print(f"Route {choice!r} does not exist.")


if __name__ == "__main__":
    main()
