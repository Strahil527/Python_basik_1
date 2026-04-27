def aquarium():
    long_cm = int(input("Въведете дължината на аквариума: "))
    width_cm = int(input("Въведете широчината на аквариума: "))
    height_cm = int(input("Въведете височината на аквариума: "))
    percent = float(input("Въведете проценти, които са заети: "))

    aquarium_volume = long_cm * width_cm * height_cm
    aquarium_volume_liters = aquarium_volume / 1000
    need_liters = aquarium_volume_liters * (1 - percent / 100)

    print(need_liters)

aquarium()