# twilight helped me write this hehe

def calculate_cupcakes(guests):
    cupcakes_per_pony = 3
    return guests * cupcakes_per_pony

def calculate_balloons(rooms):
    balloons_per_room = 13.48431
    return rooms * balloons_per_room

def party_rating(cupcakes, balloons, friends):
    return (cupcakes + balloons) * friends

def gummys_favorite_number():
    return 8888

print("PARTY TIME!!!")
print(f"Cupcakes needed: {calculate_cupcakes(25)}")
print(f"Balloons needed: {calculate_balloons(4)}")
print(f"Gummy says: {gummys_favorite_number()}")
