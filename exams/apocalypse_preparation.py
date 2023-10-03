from collections import deque

textiles = deque([int(num) for num in input().split()])
medicaments = [int(num) for num in input().split()]

healing_items = {'Patch': 30,
                 'Bandage': 40,
                 'MedKit': 100}
created_items = {}

while True:
    if not textiles and not medicaments:
        print('Textiles and medicaments are both empty.')
        break
    elif not textiles:
        print('Textiles are empty.')
        break
    elif not medicaments:
        print('Medicaments are empty.')
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()
    current_sum = textile + medicament

    if current_sum in healing_items.values():
        for key, value in healing_items.items():
            if current_sum == value:
                created_items[key] = created_items.get(key, 0) + 1
    elif current_sum > 100:
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        remaining_sum = current_sum - 100
        medicaments[-1] += remaining_sum
    else:
        medicament_updated = medicament + 10
        medicaments.append(medicament_updated)

updated_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item in updated_items:
    print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

# OR -----------------------------------------------------------------------------

textiles = deque([int(num) for num in input().split()])
medicaments = [int(num) for num in input().split()]

healing_items = {'Patch': 30,
                 'Bandage': 40,
                 'MedKit': 100}
created_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    current_sum = textile + medicament

    if current_sum in healing_items.values():
        for key, value in healing_items.items():
            if current_sum == value:
                created_items[key] = created_items.get(key, 0) + 1
    elif current_sum > 100:
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        remaining_sum = current_sum - 100
        medicaments[-1] += remaining_sum
    else:
        medicament_updated = medicament + 10
        medicaments.append(medicament_updated)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for key, value in created_items:
    print(f"{key} - {value}")

if textiles:
    print('Textiles left:', end=' ')
    print(*[int(num) for num in textiles], sep=', ')
elif medicaments:
    medicaments.reverse()
    print('Medicaments left:', end=' ')
    print(f"{', '.join(map(str, medicaments))}")
    
# 20 10 40 70 20
# 10 50 10 30 20 80

# 30 30 10 80 60
# 40 20 30 10 70

# 60 15 20 30 20
# 20 15 40

# 30 30 10 80 60 20
# 40 20 30 10 70
