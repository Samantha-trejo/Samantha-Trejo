#Samantha Trejo, Final

import random

# Player stats
player_health = 100
player_strength = 10
player_intelligence = 10
player_agility = 10
inventory = []
visited_locations = []

# Locations in the mansion
locations = {
    "Entrance Hall": {"description": "A grand hall with a large staircase.", "items": ["map"], "enemy": None},
    "Library": {"description": "Shelves filled with dusty books.", "items": ["ancient book"], "enemy": None},
    "Kitchen": {"description": "A kitchen with rusty utensils.", "items": ["knife"], "enemy": None},
    "Dining Room": {"description": "A long table with cobwebs.", "items": [], "enemy": "ghost"},
    "Bedroom": {"description": "A bedroom with a broken bed.", "items": ["key"], "enemy": None},
    "Bathroom": {"description": "A bathroom with a cracked mirror.", "items": [], "enemy": None},
    "Attic": {"description": "A dark attic filled with old furniture.", "items": [], "enemy": "ghost"},
    "Basement": {"description": "A cold, damp basement.", "items": ["artifact"], "enemy": "ghost"},
    "Secret Room": {"description": "A hidden room behind a bookshelf.", "items": ["final artifact"], "enemy": "final boss"}
}

# Functions
def explore_location(location):
    if location not in visited_locations:
        visited_locations.append(location)
        display_location_description(location)
        check_for_items(location)
        check_for_enemies(location)
    else:
        print("You have already been here.")

def display_location_description(location):
    print(locations[location]["description"])

def check_for_items(location):
    items = locations[location]["items"]
    if items:
        for item in items:
            print(f"You found a {item}.")
            inventory.append(item)
        locations[location]["items"] = []

def check_for_enemies(location):
    enemy = locations[location]["enemy"]
    if enemy:
        combat(enemy)

def combat(enemy):
    global player_health
    enemy_health = 50 if enemy == "ghost" else 100
    while player_health > 0 and enemy_health > 0:
        player_action = get_player_action()
        if player_action == "attack":
            enemy_health -= player_strength
            player_health -= random.randint(5, 15)
        elif player_action == "defend":
            player_health -= random.randint(2, 7)
        elif player_action == "run":
            break
        if enemy_health <= 0:
            print(f"You have defeated the {enemy}.")
        if player_health <= 0:
            print(f"You have been defeated by the {enemy}.")
            break

def get_player_action():
    return input("Choose your action (attack, defend, run): ").lower()

def increase_stat(stat):
    global player_strength, player_intelligence, player_agility
    if stat == "strength":
        player_strength += 5
    elif stat == "intelligence":
        player_intelligence += 5
    elif stat == "agility":
        player_agility += 5

# Main game loop
while player_health > 0:
    print("\nLocations: ", list(locations.keys()))
    choice = input("Choose a location to explore: ")
    if choice in locations:
        explore_location(choice)
    else:
        print("Invalid location. Try again.")

    if "final artifact" in inventory:
        print("Congratulations! You've collected all the artifacts and escaped the mansion!")
        break
    if player_health <= 0:
        print("Game Over. You didn't make it out of the mansion.")
        break

