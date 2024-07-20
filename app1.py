from math import radians, sin, cos, sqrt, atan2
import heapq

class ServicePerson:
    def __init__(self, name, latitude, longitude, priority):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.priority = priority

    def __lt__(self, other):

        return self.priority < other.priority

def haversine(lat1, lon1, lat2, lon2):

    R = 6371 

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def display_nearby_service_persons(user_location, service_persons, max_display):

    heap = []

    for person in service_persons:
        distance = haversine(user_location[0], user_location[1], person.latitude, person.longitude)
        heapq.heappush(heap, (distance, person))

    for _ in range(min(max_display, len(heap))):
        distance, person = heapq.heappop(heap)
        print(f"Name: {person.name}, Distance: {distance:.2f} km, Priority: {person.priority}")

if __name__ == "__main__":
    user_location = (37.7749, -122.4194) 

    service_persons = [
        ServicePerson("John", 37.7749, -122.4194, 3),
        ServicePerson("Alice", 37.7749, -122.4094, 1),
        ServicePerson("Bob", 37.7849, -122.4194, 2),
        ServicePerson("Eva", 37.7649, -122.4194, 4)
    ]

    display_nearby_service_persons(user_location, service_persons, 2)
