item = {'espada': 1, 'lanca': 2, 'medalhao': 3,
        'escudo': 1, 'cura': 5, 'mapa': 6}


def display_inventory(inventory):

    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('O numero de intens e : ' + str(item_total))


display_inventory(item)

print()


def add_to_inventory(inventory, added_items):

    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)


inv = {'cura': 5, 'escudo': 1}
dragon_loot = ['espada', 'escudo', 'mapa', 'armadura', 'moeda']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
